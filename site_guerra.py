from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route("/historia")
def historia():
    return render_template('historia.html')


@app.route("/quiz")
def quiz():
    return render_template('quiz.html')


@app.route("/quiz/errado")
def errado():
    return render_template('errado.html')


@app.route("/quiz/correto")
def correto():
    return render_template('correto.html')


@app.route("/livros")
def livros():
    return render_template('livros.html')


@app.route("/imagens")
def imagens():
    return render_template('imagens.html')


if __name__ == '__main__':
    app.run(debug=True)
