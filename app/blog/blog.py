from flask import render_template, Blueprint, request

blog_bp = Blueprint('blog_bp', __name__, template_folder='templates')

@blog_bp.route("/blogs", methods=["GET"])
def blogs():
    if request.method == "GET":
        return render_template("blog.html")

@blog_bp.route("/blogs/development", methods=["GET"])
def development():
    if request.method == "GET":
        return render_template("development.html")

@blog_bp.route("/blogs/freelance-advice-badnews-first", methods=["GET"])
def freelanceAdviceOne():
    if request.method == "GET":
        return render_template("freelance-advice-1.html")