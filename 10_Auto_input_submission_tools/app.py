
from flask import Flask, render_template, flash, redirect, url_for
import json
from flask_security import Security, roles_required, login_required
from models import User, Role
from forms import ContactForm, LoginForm, RegistrationForm, ResetPasswordForm, ForgotUsernameForm
from config import SECRET_KEY, RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY, SECURITY_PASSWORD_SALT, \
    RECAPTCHA_PARAMETERS, SECURITY_PASSWORD_HASH, SECURITY_REGISTERABLE, SECURITY_RECOVERABLE, SECURITY_CHANGEABLE

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['RECAPTCHA_PUBLIC_KEY'] = RECAPTCHA_PUBLIC_KEY
app.config['RECAPTCHA_PRIVATE_KEY'] = RECAPTCHA_PRIVATE_KEY
app.config['SECURITY_PASSWORD_SALT'] = SECURITY_PASSWORD_SALT
app.config['RECAPTCHA_PARAMETERS'] = RECAPTCHA_PARAMETERS 
app.config['SECURITY_PASSWORD_HASH'] = SECURITY_PASSWORD_HASH 
app.config['SECURITY_REGISTERABLE'] = SECURITY_REGISTERABLE
app.config['SECURITY_RECOVERABLE'] = SECURITY_RECOVERABLE
app.config['SECURITY_CHANGEABLE'] = SECURITY_CHANGEABLE

# Load user data from JSON file
with open('users.json') as json_file:
    users = json.load(json_file)

# Initialize Flask-Security with custom User and Role classes
user_datastore = {'users': users, 'roles': {}}
security = Security(app, user_datastore)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Process password reset logic here
        flash('An email with password reset instructions has been sent!', 'success')
        return redirect(url_for('index'))
    return render_template('reset_password.html', form=form)

@app.route('/forgot_username', methods=['GET', 'POST'])
def forgot_username():
    form = ForgotUsernameForm()
    if form.validate_on_submit():
        # Process username retrieval logic here
        flash('Your username has been sent to your email!', 'success')
        return redirect(url_for('index'))
    return render_template('forgot_username.html', form=form)

@app.route('/dashboard')
@login_required
@roles_required('admin')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port= 1234)
