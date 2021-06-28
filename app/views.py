from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for 

from flask_login import login_user, logout_user
from .models import User
from .forms import LoginForm, RegisterForm
from app.consts import *

from ._init_ import login_manager

page = Blueprint('page', __name__)

@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)

@page.route('/articles')
def article():
    return render_template('article.html', title = 'Article' )

@page.route('/current-post')
def currentpost():
    return render_template('current-post.html', title = 'Post' )


@page.app_errorhandler(404)
def page_not_found(error):
    return render_template ('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title = 'Index' ) 

@page.route('/logout')
def logout():
    logout_user()
    flash (LOGOUT)
    return redirect(url_for('.login'))

@page.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    
    if request.method == 'POST' and form.validate():
        user = User.get_by_username(form.username.data)
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash(LOGIN)
        else:
            flash(ERROR_USER_PASSWORD, 'error')

    return render_template('auth/login.html', title = 'Login', form = form) 

@page.route('/register', methods = ['GET', 'POST'])   
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.create_element(form.username.data, form.password.data, form.email.data)
            flash(USER_CREATED)


    return render_template('auth/register.html', title='Registro', form = form) 
