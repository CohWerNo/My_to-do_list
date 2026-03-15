from flask import render_template

def Page():
    return render_template("main/index.html", title="New Title")