####################################
# Run using(if app.run not used):  #
# flask --app hello run            #
####################################
from flask import Flask

app = Flask(__name__)


# decorator
@app.route("/") # when user goes to this path run below method
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run() # runs the file with python <file_name>.py