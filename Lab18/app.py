from flask import Flask

# Example 1: Basic “Hello, World!” Flask Application
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

if __name__ == "__main__":
    app.run(debug=True)

# Example 2: Dynamic Routes and URL Parameters
from markupsafe import escape

app = Flask(__name__)

@app.route("/greet/<name>")
def greet(name):
    return f'<h2>Hello, {escape(name.capitalize())}!</h2>'

if __name__ == "__main__":
    app.run(debug=True)

# Example 3: Template Rendering with Jinja2
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    names = ['Aktilek', 'Arsen', 'Nurik', 'Erjan']
    return render_template('index.html', names=names, title="Welcome")

if __name__ == "__main__":
    app.run(debug=True)