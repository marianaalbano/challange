from flask import Blueprint, render_template
from admin_required import admin_required


from flask_login import LoginManager, login_required, login_user, logout_user


quiz = Blueprint('quiz', __name__)

@quiz.route("/admin/quiz", methods=["GET"])
@login_required
@admin_required
def list_quiz():
    return render_template("admin/quiz/quizList.html")

@quiz.route("/admin/quiz/new", methods=["GET"])
@login_required
@admin_required
def new_quiz():
    return render_template("admin/quiz/quizNew.html")


@quiz.route("/admin/quiz/id/edit", methods=["POST"])
@login_required
@admin_required
def edit_quiz(id):
    return "edit quiz"

@quiz.route("/admin/quiz/id/remove")
@login_required
<<<<<<< HEAD
def remove_quiz(id):
=======
@admin_required
def new_quiz(id):
>>>>>>> ca7e7298010f040114594be842a8764a9ac1f7a8
    return " delete quiz"


if __name__ == "__main__":
    app.run(debug=True)