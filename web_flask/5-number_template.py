#!/usr/bin/python3
"""Starts a Flask web applicaton: HTML page"""
from flask import Flask, abort
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    prints the return value
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    prints the HBNB text
    """
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """
    prints a C, then the value of the text variable
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Prints 'Python', then value of the text variable"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<n>')
def is_number(n):
    """
    Prints "n is a number" where n is an integer
    """
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)


@app.route('/number_template/<int:n>')
def number_template(n=None):
    """Displays an HTML page"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
