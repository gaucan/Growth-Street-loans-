from app import app, lm, db
from .forms import LoginForm, RegForm, LoanForm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from .models import User, Loan


@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

# index view function suppressed for brevity
@app.route('/')
@app.route('/index', methods=['GET'])
@login_required
def index():
    loans = Loan.query.filter_by(user_id=g.user.id).all()

    return render_template('index.html',
                           title='Home',
                           user=g.user,
                           loans=loans)
"""
Loan - create new loan
"""
@app.route('/loan', methods=['GET', 'POST'])
@login_required
def loan():
  form = LoanForm()
  if form.validate_on_submit():
    loan = Loan( 
          days=form.days.data ,
          reason=form.reason.data ,
          amount=form.amount.data, 
          user_id=g.user.id ,
        )
    db.session.add(loan)
    db.session.commit()
    return redirect(url_for('index'))

  return render_template('loan.html',
                           title='Loan',
                           user=g.user,
                           form=form
                           )
"""
Shows all loans , only admin can access
"""
@app.route('/admin_loans', methods=['GET', 'POST'])
@login_required
def admin_loans():

  #verify if user is admin
  user = User.query.filter_by(email=g.user.email).first()
  if user.id != 1 :
    flash('Only admin can access this page.')
    return redirect(url_for('index'))

  loans = Loan.query.all()

  return render_template('admin_loans.html',
                           title='All loans',
                           loans=loans)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        flash('Login requested for email="%s"' %
              (email))
        user = User.query.filter_by(email=email).first()
        if user is None:
          flash('Invalid login. Please try again.')
          return redirect(url_for('login'))
        login_user(user)
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
      email=form.email.data
      user = User.query.filter_by(email=email).first()
      # control if is already registrated
      if user is  None:
        user = User( 
          buss_name=form.buss_name.data ,
          address=form.address.data ,
          company_number=form.company_number.data, 
          buss_sector=form.buss_sector.data ,
          name=form.name.data ,
          phone=form.phone.data, 
          email=form.email.data,
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful for email="%s"' %
              (email))
        login_user(user)
        return redirect('/index')
      # user already existed 
      flash('User with  email="%s" already exists.' %
              (email))
    return render_template('register.html', 
                           title='Register',
                           form=form)