# used to store standard roots for users to access i,e the home page

from flask import Blueprint

views_blueprint = Blueprint('views', __name__)

# goes to the route / and calls home function
@views_blueprint.route('/')
def home():
    return "<h1>Test</h1>"


