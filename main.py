from flask import Flask, render_template

app = Flask(__name__, template_folder="htmlFile", static_folder="htmlFile")

def regusterAllPage():
    import htmlFile.taskList.list0.index as list0
    app.register_blueprint(list0.pageBP)
regusterAllPage()

@app.route("/")
def index():
    import htmlFile.main.index as main
    return main.Page()

if __name__ == "__main__":
    app.run(debug=True)