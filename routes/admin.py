from flask import Blueprint, render_template
from admin_required import admin_required


from flask_login import LoginManager, login_required, login_user, logout_user


admin = Blueprint('admin', __name__)

@admin.route("/admin/main")
@login_required
@admin_required
def admin_home():
    return render_template("admin/main.html")