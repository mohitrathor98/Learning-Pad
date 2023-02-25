from flask import Flask, render_template

app = Flask(__name__)

# doc: https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates

# All HTML files under templates directory
# All CSS, images, etc under static directory
# Path in the HTMl file should be static/file_name

# if static file not being rendered after change: do a hard refresh, shift+refresh

@app.route('/')
def home():
    # this will render the page inside templates directory
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)