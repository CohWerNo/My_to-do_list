from flask import Flask, render_template

app = Flask(__name__, template_folder="htmlFile", static_folder="htmlFile")

def regusterAllPage():
    import htmlFile.taskList.list1.index as list1
    app.register_blueprint(list1.pageBP)
regusterAllPage()

@app.route("/")
def index():
    import htmlFile.main.index as main
    return main.Page()

if __name__ == "__main__":
    app.run(debug=True)