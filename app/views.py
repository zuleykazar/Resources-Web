from flask import Blueprint
from flask import render_template, request, flash 

from .models import User
from .forms import LoginForm, RegisterForm

page = Blueprint('page', __name__)

@page.route('/article')
def article():
    return render_template('article.html', title = 'Article' ) #el title no se esta mostrando (Issue)

@page.app_errorhandler(404)
def page_not_found(error):
    return render_template ('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title = 'Index' ) #el title no se esta mostrando

@page.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    
    if request.method == 'POST' and form.validate():
        user = User.get_by_username(form.username.data)
        if user and user.verify_password(form.password.data):
            flash('Usuario autenticado exitosamente.')
    
    return render_template('auth/login.html', title = 'Login', form = form) #el title no se esta mostrando

@page.route('/register', methods = ['GET', 'POST'])   
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.create_element(form.username.data, form.password.data, form.email.data)
            print('Usuario creado exitosamente!')
            print(user.id)

    return render_template('auth/register.html', title='Registro', form = form) #el title no se esta mostrando

