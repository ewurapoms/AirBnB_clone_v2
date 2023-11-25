#!/usr/bin/python3
"""Starts a Flask web applicaton: n = int"""
from flask import Flask
from flask import abort

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
