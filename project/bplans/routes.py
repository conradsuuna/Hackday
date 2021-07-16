from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from project import db
from project.models import Bplan
from project.bplans.forms import BplanForm

bplans = Blueprint('bplans', __name__)


@bplans.route("/bplan/new", methods=['GET', 'POST'])
@login_required
def new_bplan():
    form = BplanForm()
    if form.validate_on_submit():
        bplan = Bplan(title=form.title.data, industry=form.industry.data, owner=current_user,content=form.content.data, funds_needed=form.funds_needed.data)
        db.session.add(bplan)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_bplan.html', title='New Business Plan',
                           form=form, legend='New B-Plan')


@bplans.route("/bplan/<int:bplan_id>")
def bplan(bplan_id):
    bplan = Bplan.query.get_or_404(bplan_id)
    return render_template('bplan.html', title=bplan.title, bplan=bplan)


@bplans.route("/post/<int:bplan_id>/update", methods=['GET', 'POST'])
@login_required
def update_bplan(bplan_id):
    bplan = Bplan.query.get_or_404(bplan_id)
    if bplan.owner != current_user:
        abort(403)
    form = BplanForm()
    if form.validate_on_submit():
        bplan.title = form.title.data
        bplan.content = form.content.data
        bplan.industry = form.industry.data
        bplan.funds_needed = form.funds_needed.data
        db.session.commit()
        flash('Your plan has been updated!', 'success')
        return redirect(url_for('bplans.bplan', bplan_id=bplan.id))
    elif request.method == 'GET':
        form.title.data = bplan.title
        form.content.data = bplan.content
    return render_template('create_bplan.html', title='Update Biz Plan',
                           form=form, legend='Update Biz plan')


@bplans.route("/bplan/<int:bplan_id>/delete", methods=['POST'])
@login_required
def delete_bplan(bplan_id):
    bplan = Bplan.query.get_or_404(bplan_id)
    if bplan.owner != current_user:
        abort(403)
    db.session.delete(bplan)
    db.session.commit()
    flash('Your business plan has been deleted!', 'success')
    return redirect(url_for('main.home'))
