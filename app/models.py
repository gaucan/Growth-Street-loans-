from app import db


# email, buss_name, address, company_number, buss_sector, name, phone

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), index=True, unique=True)
	buss_name = db.Column(db.String(64), index=True, unique=True)
	address = db.Column(db.String(64), index=True, unique=True)
	company_number = db.Column(db.String(64), index=True, unique=True)
	buss_sector = db.Column(db.String(64), index=True, unique=True)
	name = db.Column(db.String(64), index=True, unique=True)
	phone = db.Column(db.String(64), index=True, unique=True)
	loans = db.relationship('Loan', backref='borrower', lazy='dynamic')

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
		    return unicode(self.id)  # python 2
		except NameError:
		    return str(self.id)  # python 3

	def __repr__(self):
		return '<User %r>' % (self.name)

class Loan(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.String(64), index=True, unique=True)
	days = db.Column(db.String(64), index=True, unique=True)
	reason = db.Column(db.String(64), index=True, unique=True)
	user_id  = db.Column(db.Integer, db.ForeignKey("user.id"))

	def __repr__(self):
		return '<Loan %r>' % (self.id)
