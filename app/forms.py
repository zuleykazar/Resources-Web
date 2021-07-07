from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField

from .models import User 

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El campo debe contener entre 4 y 50 caracteres.')
    ])
    password = PasswordField('Password', [
        validators.Required(message='El password es requerido.') #no muestra este mensaje (Issue)
    ])

      
class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El campo debe contener entre 4 y 50 caracteres.')
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido.'), #no muestra este mensaje (Issue)
        validators.Email(message='Ingrese un email válido.') #no muestra este mensaje (Issue)
    ])
    password = PasswordField('Password', [
        validators.Required('El password es requerido.'), #no muestra este mensaje (Issue)
        validators.EqualTo('confirm_password', message='La contraseña no coincide.')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('', [
        validators.DataRequired()
    ])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso.') #no muestra este mensaje (Issue)

    def validate_username(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El email ya se encuentra en uso.') #no muestra este mensaje (Issue) 

    def TaskForm(Form):
        title = StringField('Titulo', [
            validators.lenght(min=4, max=50, message='Título fuera de rango.'),
            validators.DataRequired(message='El título es requerido.')
        ])
        description = TextAreaField('Descripción', [
            validator.DataRequired(message='La descripción es requerida.')
        ])             