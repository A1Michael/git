from flask import Blueprint

authentication_Blueprint = Blueprint('auth', __name__)

@authentication_Blueprint.route('/login')
def login():
    return "<p>Login</p>"

@authentication_Blueprint.route('/logout')
def logout():
    return "<p>Logout</p>"

@authentication_Blueprint.route('/Register')
def register_account():
    return "<p>Register</p>"