from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from admin_required import admin_required
from controllers.Users import User
from controllers.QuizController import QuizController
from model.Users import db

user = Blueprint('user', __name__)

@user.route("/user/<id>", methods=['GET', 'POST'])
@login_required
def change_profile_user(id):
    usuario = User()
    if request.method == 'POST':
        usuario.updateUser(id, request.form)
        return render_template("edituser")
    else:
        usuario = usuario.findOne(id)
        return render_template('edituser', usuario=usuario)

@user.route("/user/<id>/quizzes", methods=["GET"])
@login_required
def user_quizzes(id):
    quizzes = User()
    quizzes = quizzes.findUserQuiz(id)
    return render_template("user/quizzes/quizList.html", quizzes=quizzes)


@user.route("/user/quiz/<id_quiz>/questions", methods=["GET", "POST"])
@login_required
def user_response(id_quiz):
    questions = QuizController()
    questions = questions.findOne(id_quiz)
    return render_template("user/quizzes/quizPlay.html", questions=questions)