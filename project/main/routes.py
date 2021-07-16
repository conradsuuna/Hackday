from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import current_user
from project.models import Bplan

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template('home.html')
    return render_template('user.login')


@main.route("/about")
def about():
    return render_template('about.html', title='About')