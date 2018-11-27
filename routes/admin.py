from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from admin_required import admin_required
from controllers.Users import User
from controllers.ResponseController import ResponseController

from controllers.QuizController import QuizController

from controllers.QuestionsDisserty import QuestionsDisserty
from controllers.QuestionsMultiple import QuestionsMultiple

from model.Users import db

from controllers.Email import Email


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
        #email = Email()
        #email.sendEmaiil(request.form)
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
        for quiz in quizzes:
            pass
            
        return render_template("admin/userEdit.html", usuario=usuario, quizzes=quizzes)


@admin.route("/admin/user/<id>/remove")
@login_required
@admin_required
def delete_user(id):
    usuario = User()
    usuario = usuario.removeUser(id)
    return redirect('/admin/users')


@admin.route("/admin/results")
@login_required
@admin_required
def results_all():
    try:
        results = []

        response = ResponseController()
        user_response = response.findAll()
        
        questions_disserty = QuestionsDisserty()
        questions_multiple = QuestionsMultiple()

        # percorre todos os dicionarios do MongoDB
        for u in user_response:   
            right = []

            # percorre as questoes de um unico usuario
            for question in u["questions"]:
                
                # verifica se a questao multipla escolha esta correta
                id_question = int(question["id_question"])
                if question["type"] == "multiple":
                    q = questions_multiple.findOne(id_question)
                    if q.right_question == question["response"]:
                        right.append(question)

                # verifica se a questao dissertativa esta correta
                elif question["type"] == "disserty":
                    q = questions_disserty.findOne(id_question)
                    if q.right_question == question["response"]:
                        right.append(question)

            # faz uma contagem de quantas questoes estao corretas
            total = len(right)

            # busca as questoes atreladas ao quiz
            disserty = questions_disserty.findByQuiz(u["id_quiz"])
            multiple = questions_multiple.findByQuiz(u["id_quiz"])

            # verifica o total de questoes existentes
            total_questions = len(disserty) + len(multiple)

            # monta o json para retorno
            right_question = {"name":u["name"],
                        "email": u["email"],
                        "name_quiz": u["name_quiz"],
                        "right_question": total,
                        "total_questions": total_questions}

            results.append(right_question)

    except Exception as e:
        print (e)


    return render_template("admin/results/userResults.html", results=results)



