#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask
from markupsafe import escape
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_ever(n):
    """/number_odd_or_even/<int:n> route"""
    if n % 2 == 0:
        t = "even"
    else:
        t = "odd"
    return render_template('6-number_odd_or_even.html', number=n, type=t)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
