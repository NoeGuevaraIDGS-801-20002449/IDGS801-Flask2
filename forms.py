from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, FormField, SelectField,IntegerField

from wtforms.fields import EmailField, TextAreaField, RadioField,PasswordField,FieldList
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

    
class UserForm(Form):
    matricula=StringField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')])
    amaterno=StringField('Amaterno',[mi_validacion])
    apaterno=StringField('Apaterno')
    email=EmailField('Correo')

class FormC(Form):
    numCaja=IntegerField('Numero De Cajas')
    tCaja=FieldList(StringField('numero'))


class LoginForm(Form):
    username=StringField('usuario',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')])
    password=StringField('contraseña',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 4 min and 5 max')])