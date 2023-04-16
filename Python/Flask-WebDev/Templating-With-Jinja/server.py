from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    # render_template takes template name and
    # **kwargs as argument: multiple key=value pairs, which
    # can be used in the template files
    today = datetime.today()
    return render_template("hello.html", num=10, name="Mohit", year=today.year)


@app.route("/forloop")
def forloop():
    return render_template(
        "Loop.html",
        fruits=["Mangoes", "Apples", "Oranges"]
    )


@app.route("/ifelse")
def ifelse():
    return render_template(
        "IfElse.html",
        nums=[2, 3, 4, 5]
    )


if __name__ == "__main__":
    app.run(debug=1)
