#!/usr/bin/python3
"""Starts a Flask web applicaton"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
