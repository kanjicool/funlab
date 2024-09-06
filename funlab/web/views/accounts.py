from urllib import response
from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    session,
    current_app,
    send_file,
    abort,
)
from flask_login import login_user, logout_user, login_required, current_user
from funlab import models
from .. import forms


module = Blueprint("accounts", __name__)

@module.route("/", methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    user = models.User.objects(username=form.username.data).first() 

    return render_template("/accounts/login.html", form=form, user=user)