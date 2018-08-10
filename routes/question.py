from flask import Blueprint, render_template, redirect, request
from admin_required import admin_required
from controllers.QuestionsDisserty import QuestionsDisserty 
from controllers.QuizController import QuizController 

from controllers.QuestionsMultiple import QuestionsMultiple
from controllers.QuizController import QuizController


from flask_login import LoginManager, login_required, login_user, logout_user


question = Blueprint('question', __name__)

@question.route("/admin/quiz/<id>/questions", methods=["GET"])
@login_required
@admin_required
def list_question(id):

    q_disserty = QuestionsDisserty()
    q_disserty = q_disserty.findByQuiz(id)
    
    q_multiple = QuestionsMultiple()
    q_multiple = q_multiple.findByQuiz(id)


    return render_template("admin/quiz/quizList.html", q_multiple=q_multiple, q_disserty=q_disserty)

@question.route("/admin/quiz/<id>/questions/new", methods=["GET", "POST"])
@login_required
@admin_required
def add_question(id):
    if request.method == 'POST':
        if request.form["type"] == "multiple":
            q_multiple = QuestionsMultiple()
            q_multiple.insertQM(id,request.form)
        else:
            q_disserty = QuestionsDisserty()
            q_disserty.insertQD(id,request.form)

        return redirect("admin/quiz/%s/edit" %id)

    else:
        quiz = QuizController()
        quiz = quiz.findOne(id)
        return render_template("admin/quiz/question/questionNew.html", quiz=quiz)

@question.route("/admin/quiz/<id>/questions_multiple/<id_question>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_multiple(id, id_question):
    q_multiple = QuestionsMultiple()

    if request.method == 'POST':
        q_multiple.updateQM(id,request.form)
        return redirect("/admin/quiz/%s/questions" %id)
        
    else:
        questions = q_multiple.findOne(id_question)
        return render_template("admin/quiz/<id>/questionEdit.html", questions=questions)


@question.route("/admin/quiz/<id>/questions_disserty/<id_question>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_disserty(id, id_question):
    q_disserty = QuestionsDisserty()

    if request.method == 'POST':
        q_disserty.updateQD(id,request.form)
        return redirect("/admin/quiz/%s/questions" %id)
        
    else:
        questions = q_disserty.findOne(id_question)
        return render_template("admin/quiz/<id>/questionEdit.html", questions=questions)

@question.route("/admin/quiz/<id>/questions/<id_question>/remove")
@login_required
@admin_required
def remove_question(id, id_question):
    if request.method == 'POST':
        if request.form["type"] == "multiple":
            q_multiple = QuestionsMultiple()
            q_multiple.removeQM(id)
            
        else:
            q_disserty = QuestionsDisserty()
            q_disserty.removeQD(id)

        return redirect("/admin/quiz/%s/questions" %id)

    else:
        return render_template("admin/quiz/questionRemove.html")
