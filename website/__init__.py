from flask import Flask
from .views import views_blueprint
from .auth import authentication_Blueprint
def create_app():
    # initialise app with the name of the file
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ThisIsTheKey1010'



    # the prefix is used to access all the urls 
    # The prefix is set to '/' as we are not want any prefix's
    app.register_blueprint(views_blueprint, url_prefix='/' )
    app.register_blueprint(authentication_Blueprint, url_prefix='/')
    
    return app