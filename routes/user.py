from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from admin_required import admin_required
from controllers.Users import User
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
    usuario = User()
    usuario = usuario.findUserQuiz(id)
    return render_template("edituser")