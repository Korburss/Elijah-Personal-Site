from flask import render_template, Blueprint, request, Response, json

from app.email import send_email

home_bp = Blueprint('home_bp', __name__, template_folder='templates')

@home_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("home.html", title="About")
    
@home_bp.route("/testimonials", methods=["GET", "POST"])
def testimonials():
    if request.method == "GET":
        return render_template("testimonials.html", title="Testimonials")

@home_bp.route("/development", methods=["GET", "POST"])
def development():
    if request.method == "GET":
        return render_template("development.html", title="Site Creation")
    
@home_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title="Contact Me")
    if request.method == "POST":
        data = request.form
        send_email(data)
        return "200"
    