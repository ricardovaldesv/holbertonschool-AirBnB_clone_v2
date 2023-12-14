#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_Hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Phyton_is_cool(text):
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    return f'{escape(n)} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
