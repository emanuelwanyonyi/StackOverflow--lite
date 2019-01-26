from flask import Blueprint, render_template, flash, redirect
from flask import jsonify, request, make_response
import jwt
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from StackOverflow import app


blueprint = Blueprint('site', __name__, template_folder='template')
Bootstrap(app)

@blueprint.route('/')
def home():
    return render_template('index.html')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=4, max=40)])
    email = StringField('Email', validators=[InputRequired(), Length(min=4, max=40), Email(message='Invalid email!')])
    password  = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

class LoginFrom(FlaskForm):
    email = StringField('username', validators=[InputRequired(), Length(min=4, max=40), Email(message='Invalid email!')])
    password  = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember_me = BooleanField('remember me')

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return 'Form Successfully Submitted!'
    return render_template('register.html', form=form)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        flash('Login requested for use {}, remember_me=()'.format(
          form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', form=form)

@blueprint.route('/dashboard')
#@login_reqyired
def dashboard():
    return render_template('dashboard.html')

@blueprint.route('/about')
def about():
    return render_template('about.html')

'''
@blueprint.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        header = {
                  'typ' : 'JWT',
                  'alg' : 'HS256'
                 }

        payload = {
                   'user' : auth.username,
                   'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
                  }

        s = base64Encode(header) + "." + base64Encode(payload)
        token = hashAlgHs256(s, secret)
        
        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW.Authenticate': Basic realm="Login Required"})
    '''