from flask import Flask

app = Flask(__name__)

def bold_decorator(function):
    def wrapper():
        return '<b>'+function()+'</b>'
    return wrapper

def emphasis(function):
    def wrapper():
        return '<em>'+function()+'</em>'
    return wrapper

def underline(function):
    def wrapper():
        return '<u>'+function()+'</u>'
    return wrapper

@app.route('/')
@underline # 3) lastly this decorator
@emphasis # 2) then this decorator
@bold_decorator # 1) first this gets called
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True)