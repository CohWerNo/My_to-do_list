from flask import Blueprint, render_template

pageBP = Blueprint("pageBP", __name__)

@pageBP.route("/Page")
def Page():
    return render_template("main/index.html", title="New Title")