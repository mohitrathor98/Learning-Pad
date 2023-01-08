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
### default type is string

#### path: takes a path as input. Ex: /username/<path:name>. Now we can
#####      give url such as localhost:5000/username/mohit/rathor, "mohit/rathor" will be input

#### uuid: A universally unique identifier is a 128-bit label used for information in computer systems.
#####      Generally used for identifying information that needs to be unique within a system or network thereof.

##### We can also give multiple variables in same path: Ex: /username/<name>/<int:age>

@app.route("/username/<name>")
def username(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    # set debug property to true 
    # to auto-restart server with changes
    # and get debug messages in the browser
    app.run(debug=True)