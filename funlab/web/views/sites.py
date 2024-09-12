from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

module = Blueprint("site", __name__)


@module.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("accounts.login"))
    else:
        return redirect(url_for("dashboard.index"))