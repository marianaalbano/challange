from model import db, app
from flask import Flask, request, render_template


# app = Flask(__name__)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        if request.form['username'] == "admin" and request.form["password"] == "admin":
            return render_template("homeadmin.html")
        elif request.form['username'] == "user" and request.form["password"] == "user":
            return render_template("homeUser.html")
    else:
        return render_template("login.html")

@app.route("/logoff", methods=["GET"])
def logoff():
    return render_template("login.html")

@app.route("/user", methods=["GET", "POST"])
def user():
    if request.method == 'POST':
        return "adicionando usuario"
    else:
        return "listando user"

@app.route("/user/id", methods=["GET", "POST"])
def edit_user():
    if request.method == 'POST':
        return "Editando usuario"
    else:
        return "edit user"

@app.route("/user/id/remove")
def delete_user():
    return "delete user"



if __name__ == "__main__":
    app.run(debug=True)


