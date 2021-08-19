from flask import request, Blueprint, render_template
from flask_user import login_required

def get_home_blueprint():
    home = Blueprint('home', __name__)

    @home.route('/')
    @login_required
    def route_home():
        return render_template('home.html')

    return home