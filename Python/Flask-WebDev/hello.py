####################################
# Run using(if app.run not used):  #
# flask --app hello run            #
####################################
from flask import Flask

app = Flask(__name__)


# decorator function which is inside app function,
# which lives inside Flask class
@app.route("/") 
# when user goes to this path run below method
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "Bye!!"


# if user gives a route not defined in the application
@app.errorhandler(404)
def pageNotFound():
    return "<h1>Sorry! This route is not handled."


if __name__ == "__main__":
    app.run()
    # runs the file with python <file_name>.py
