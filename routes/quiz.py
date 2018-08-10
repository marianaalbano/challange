from flask import Blueprint, render_template, redirect, request
from admin_required import admin_required
from controllers.QuizController import QuizController
from controllers.QuestionsMultiple import QuestionsMultiple
from controllers.QuestionsDisserty import QuestionsDisserty 



from flask_login import LoginManager, login_required, login_user, logout_user


quiz = Blueprint('quiz', __name__)

@quiz.route("/admin/quiz", methods=["GET"])
@login_required
@admin_required
def list_quiz():
    quiz = QuizController()
    quizzes = quiz.findAll()
    return render_template("admin/quiz/quizList.html", quizzes=quizzes)

@quiz.route("/admin/quiz/new", methods=["GET", "POST"])
@login_required
@admin_required
def new_quiz():
    if request.method == 'POST':
        quiz = QuizController()
        quiz.insertQuiz(request.form)
        id_quiz = quiz.findLastOne()

        return redirect("admin/quiz/%s/edit" %id_quiz.id)
    else:
        return render_template("admin/quiz/quizNew.html")


@quiz.route("/admin/quiz/<id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_quiz(id):
    quiz = QuizController()
    if request.method == 'POST':
        quiz.updateQuiz(id,request.form)
        return redirect("admin/quiz/quizList.html")
    else:
        quiz = quiz.findOne(id)
        q_disserty = QuestionsDisserty()
        q_disserty = q_disserty.findByQuiz(id)

        q_multiple = QuestionsMultiple()
        q_multiple = q_multiple.findByQuiz(id)
        return render_template("admin/quiz/quizEdit.html", quiz=quiz, q_disserty=q_disserty, q_multiple=q_multiple)

@quiz.route("/admin/quiz/<id>/remove")
@login_required
@admin_required
def remove_quiz(id):
    quiz = QuizController()
    quiz = quiz.removeQuiz(id)
    return redirect("admin/quiz")