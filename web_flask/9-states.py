#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ends database session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """shows an HTML page that lists all states & cities"""
    states = storage.all(State)
    return render_template('9-states.html', state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """prints an HTML about <id>, where existing"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
