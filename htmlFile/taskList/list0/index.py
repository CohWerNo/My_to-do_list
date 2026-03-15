from flask import Blueprint, render_template, request, jsonify
import os

pageBP = Blueprint("pageBP", __name__)
filePath = "htmlFile/taskList/list0/saveResorce/text.txt"

# создаем основную страницу с текстом
@pageBP.route("/list0")
def Page():
    with open(filePath, "r", encoding="UTF-8") as file:
        fileText = file.read()
    return render_template("taskList/list0/index.html", title="List 1", savedTextInFile=fileText)

# сохраняем всё содержимое в тексте
@pageBP.route("/save-text-in-file", methods=["POST"])
def saveTextInFile():
    data = request.get_json()

    # читаем и переписываем файл
    with open(filePath, "w", encoding="UTF-8") as file:
        fileData = file.write(data.get("text"))

    return jsonify({"status":"success"})