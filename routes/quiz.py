from flask import Blueprint, render_template, redirect, request
from admin_required import admin_required
from controllers.QuizController import QuizController


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
        quiz = quiz.insertQuiz(request.form)
        id = quiz.findLastOne()

        return redirect("admin/quiz/%s/questions" %id)
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
        return render_template("admin/quiz/quizEdit.html", quiz=quiz)

@quiz.route("/admin/quiz/<id>/remove")
@login_required
@admin_required
def remove_quiz(id):
    quiz = QuizController()
    quiz = quiz.removeQuiz(id)
    return redirect("admin/quiz")