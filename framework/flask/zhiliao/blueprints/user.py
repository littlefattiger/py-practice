from flask import Blueprint, render_template, request
from ext import mail,db
from flask_mail import Message
from models import EmailCaptchaModel
from datetime import datetime
import string, random

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route("/register")
def register():
    return render_template("register.html")


@bp.route("/captcha")
def get_captcha():
    email = request.args.get("email")
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))
    # message = Message(
    #     subject="邮箱测试",
    #     recipients=[email],
    #     body=f"your code is {captcha}",
    # )
    # mail.send(message)
    captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
    if captcha_model:
        captcha_model.captcha = captcha
        captcha_model.create_time = datetime.now()
        db.session.commit()
    else:
        captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
        db.session.add(captcha_model)
        db.session.commit()
    return "success"
