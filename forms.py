from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, FormField, SelectField,IntegerField

from wtforms.fields import EmailField, TextAreaField, RadioField,PasswordField,FieldList
from wtforms import validators

class UserForm(Form):
    matricula=StringField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=0,message='long de campo 4 min and 5 max')])

    nombre=StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=0,message='long de campo 4 min and 5 max')])
    amaterno=StringField('Amaterno')
    apaterno=StringField('Apaterno')
    email=EmailField('Correo')

class FormC(Form):
    numCaja=IntegerField('Numero De Cajas')
    tCaja=FieldList(StringField('numero'), min_entries=1, max_entries=100)

    