from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from admin_required import admin_required
from controllers.Users import User
from controllers.QuizController import QuizController
from model.Users import db


admin = Blueprint('admin', __name__)

@admin.route("/admin/main")
@login_required
@admin_required
def admin_home():
    return render_template("admin/main.html")

@admin.route("/admin/<id>", methods=['GET', 'POST'])
@login_required
@admin_required
def change_profile_admin(id):
    usuario = User()
    if request.method == 'POST':
        usuario.updateUser(id, request.form)
        return render_template("editadmin")
    else:
        usuario = usuario.findOne(id)
        return render_template('editadmin', usuario=usuario)

@admin.route("/admin/users", methods=["GET"])
@login_required
@admin_required
def user():
    usuarios = User()
    usuarios = usuarios.findAll()
    return render_template("admin/userList.html", usuarios=usuarios)


@admin.route("/admin/user/new", methods=["GET", "POST"])
@login_required
@admin_required
def new_user():
    if request.method == 'POST':
        usuario = User()
        usuario = usuario.insertUser(request.form)
        return redirect('/admin/users')
    else:
        return render_template("admin/userCadastro.html")


@admin.route("/admin/user/<id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_user(id):
    usuario = User()
    if request.method == 'POST':
        usuario = usuario.updateUser(id,request.form)
        return redirect('/admin/users')
    else:
        usuario = usuario.findOne(id)
        quiz = QuizController()
        quizzes = quiz.findAll()
        return render_template("admin/userEdit.html", usuario=usuario, quizzes=quizzes)


@admin.route("/admin/user/<id>/remove")
@login_required
@admin_required
def delete_user(id):
    usuario = User()
    usuario = usuario.removeUser(id)
    return redirect('/admin/users')
