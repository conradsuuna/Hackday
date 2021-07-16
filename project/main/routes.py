from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import current_user, login_required
from project.models import Bplan

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template('home.html')
    return render_template('login.html')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/business_plan", methods=['GET', 'POST'])
@login_required
def business_plan():
    if request.method == "POST":
        data = request.form
        new_plan = Bplan(
                        title = data['title'],
                        industry = data['industry'],
                        funds_needed = data['funds_needed'],
                        content = data['content'],
                        user_id = current_user.id,
                    )
        new_plan.save()
        return redirect('/home')
    else:
        return render_template('create_bplan.html')


@main.route("/my_plans")
@login_required
def show_business_plans():
    bplans = Bplan.query.filter_by(user_id=current_user.id)
    return render_template('bplans.html',bplans=bplans)
    