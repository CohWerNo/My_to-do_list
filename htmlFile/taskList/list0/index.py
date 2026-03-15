from flask import Blueprint, render_template, Request, jsonify

pageBP = Blueprint("pageBP", __name__)

@pageBP.route("/list0")
def Page():
    return render_template("taskList/list0/index.html", title="List 1")

@pageBP.route("/save-text-in-file", methods=["POST"])
def saveTextInFile():
    data = Request.get_json()
    print(data.text)
    #return jsonify({"status":"success"})