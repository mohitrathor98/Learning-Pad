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


if __name__ == "__main__":
    app.run(debug=1)
