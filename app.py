from controllers.Users import User
from model.Users import db, app
from routes.admin_required import admin_required
from routes.admin import admin
from routes.quiz import quiz


from datetime import timedelta
from flask import Flask, request, render_template, session,redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user



# app = Flask(__name__)

app.register_blueprint(admin)
app.register_blueprint(quiz)

app.secret_key = "challange"
app.permanent_session_lifetime = timedelta(seconds=3600)

login_manager = LoginManager()
login_manager = LoginManager(app)
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))

@login_manager.user_loader
def load_user(id):
    user = User()
    return user.findOne(id)


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        try:
            username = request.form["username"]
            password = request.form["password"]
            user = User()
            user = user.loginUser(username,password)
            if user.admin == True:
                login_user(user, remember=False)
                return redirect('/admin/main')
            elif user.admin == False:
                login_user(user, remember=False)
                return redirect('/user/main')
        except Exception as e:
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/user/main")
@login_required
def user_home():
    return render_template("user/base.html")


if __name__ == "__main__":
    app.run(debug=True)


