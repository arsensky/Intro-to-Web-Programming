from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    books = [
        {"id": 1, "title": "When the Mountains Fall", "author": "Chyngyz Aitmatov"},
        {"id": 2, "title": "1984", "author": "George Orwell"},
        {"id": 3, "title": "Fathers and Sons", "author": "Ivan Turgenev"},
    ]
    return render_template('index.html', books=books, title="Book List")

if __name__ == '__main__':
    app.run(debug=True)