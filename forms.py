from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, FormField, SelectField,IntegerField

from wtforms.fields import EmailField, TextAreaField, RadioField,PasswordField,FieldList
class UserForm(Form):
    matricula=StringField('Matricula')
    nombre=StringField('Nombre')
    amaterno=StringField('Amaterno')
    apaterno=StringField('Apaterno')
    email=EmailField('Correo')

class FormC(Form):
    numCaja=IntegerField('Numero De Cajas')
    tCaja=FieldList(StringField('numero'), min_entries=1, max_entries=100)

    