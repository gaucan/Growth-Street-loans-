 # -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, ValidationError, SelectField
from wtforms.validators import DataRequired, Length, NumberRange


def length(min=-1, max=-1):
    message = 'Registration company number is  8-digit number.'

    def _length(form, field):
        l = str(field.data) and len(str(field.data)) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)
    return _length

class RegForm(Form):
	buss_name = StringField('Bussiness name', validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	company_number = IntegerField('Registration company number', validators=[length(min=8,max=8)])
	buss_sector = SelectField("Bussiness sector: ", 
			choices=[("Retail", "Retail"), ("Professional Services", "Professional Services"),
		 (" Food & Drink", " Food & Drink"), ("Entertainment", "Entertainment")])
	name = StringField('Name', validators=[DataRequired()])
	phone = StringField('Phone number', validators=[DataRequired()])
	email = StringField('Email:', validators=[DataRequired()])

class LoginForm(Form):
	email = StringField('Email:', validators=[DataRequired()])

class LoanForm(Form):
	amount = IntegerField(u'Amount (between £10000 - £100000):', 
		validators=[NumberRange(min=10000,max=100000,message=u'Must be between £10000 and £100000.')])
	days = IntegerField('Number of days:', validators=[DataRequired()])
	reason = StringField('Reason:', validators=[DataRequired()])