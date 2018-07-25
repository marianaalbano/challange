from controllers.Users import User
from model.Users import db, app
from admin import admin_required


from datetime import timedelta
from flask import Flask, request, render_template, session,redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user



# app = Flask(__name__)

app.secret_key = "challange"

login_manager = LoginManager()


app.permanent_session_lifetime = timedelta(seconds=3600)

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
        username = request.form["username"]
        password = request.form["password"]
        user = User()
        user = user.loginUser(username,password)
        if user.admin == True:
            login_user(user, remember=False)
            return redirect(url_for('admin_home'))
        elif user.admin == False:
            login_user(user, remember=False)
            return redirect(url_for('user_home'))
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/admin/main")
@login_required
@admin_required
def admin_home():
    return render_template("admin/main.html")


@app.route("/user/main")
@login_required
def user_home():
    return render_template("user/base.html")


@app.route("/admin/users", methods=["GET"])
@login_required
@admin_required
def user():
    usuarios = User()
    usuarios = usuarios.findAll()
    return render_template("admin/userList.html", usuarios=usuarios)

@app.route("/admin/user/new", methods=["GET", "POST"])
@login_required
def new_user():
    if request.method == 'POST':
        usuario = User()
        usuario = usuario.insertUser(request.form)
        return render_template("admin/userCadastro.html")
    else:
        return render_template("admin/userCadastro.html")

@app.route("/admin/user/<id>", methods=["GET", "POST"])
@login_required
def edit_user(id):
    if request.method == 'POST':
        return "Editando usuario" 
    else:
        usuario = User()
        usuario = usuario.findOne(id)
        return render_template("admin/userList.html", usuario=usuario)


@app.route("/admin/user/<id>/remove")
@login_required
def delete_user(id):
    usuario = User()
    usuario = usuario.removeUser(id)
    return "Usuario Deletado com sucesso"


if __name__ == "__main__":
    app.run(debug=True)


