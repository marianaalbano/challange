from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from admin_required import admin_required
from controllers.Users import User
from controllers.QuizController import QuizController
from model.Users import db
from model.UserResponse import UserResponse

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
    lista = []

    user_response = UserResponse.objects(id_user='%s' %current_user.id)

    quizzes = User()
    quizzes = quizzes.findUserQuiz(id)
    print (type(user_response.count()))
    if user_response.count() > 0:
        print("cai aqui")
        for quiz_available in quizzes:
            for quiz_answered in user_response:
                if int(quiz_available.id) == int(quiz_answered["id_quiz"]):
                    print ("cai no if")
                    continue
                else:
                    print("cai no else")
                    lista.append(quiz_available)

    else:
        lista = quizzes
    
    return render_template("user/quizzes/quizList.html", quizzes=lista)

@user.route("/user/quiz/<id_quiz>/questions", methods=["GET", "POST"])
@login_required
def user_response(id_quiz):
    if request.method == "POST":
        user_response = UserResponse()

        response = []
        for responses in request.form:
            if "disserty" in responses:
                response.append({"type":"disserty", 
                                 "id_question":responses[-1], 
                                 "response":request.form[responses]})
            else:
                response.append({"type":"multiple", 
                                 "id_question":responses[-1], 
                                 "response":request.form[responses]})
                
                
        user_response.name = current_user.name
        user_response.id_user = "%s" %current_user.id
        user_response.id_quiz = id_quiz
        user_response.questions = response
        user_response.save()

        return redirect('/user/%s/quizzes' %current_user.id)
    else:
        questions = QuizController()
        questions = questions.findOne(id_quiz)
        return render_template("user/quizzes/quizPlay.html", questions=questions)