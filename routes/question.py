from flask import Blueprint, render_template
from admin_required import admin_required


from flask_login import LoginManager, login_required, login_user, logout_user


question = Blueprint('question', __name__)

@question.route("/admin/quiz/<id>/questions", methods=["GET"])
@login_required
@admin_required
def list_question(id):
    return render_template("admin/quiz/questionsList.html")

@question.route("/admin/quiz/<id>/questions/new", methods=["POST"])
@login_required
@admin_required
def add_question(id):
    return render_template("admin/quiz/questionNew.html")

@question.route("/admin/quiz/<id>/questions/<id_question>/edit", methods=["POST"])
@login_required
@admin_required
def edit_question(id, id_question):
    return render_template("admin/quiz/questionEdit.html")

@question.route("/admin/quiz/<id>/questions/<id_question>/remove")
@login_required
@admin_required
def remove_question(id, id_question):
    return render_template("admin/quiz/questionRemove.html")
