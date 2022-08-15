from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

# variable rules
### can add a variable sections to a URL by marking sections with <var_name>
### function then receives the <var_name> as keyword argument

### can specify type of argument like <converter:var_name>
### where converter is int, float, path, string, uuid 

@app.route("/username/<name>")
def username(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)