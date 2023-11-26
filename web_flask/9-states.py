#!/usr/bin/python3
"""Initiates a Flask web application.
The application is set to listen on 0.0.0.0, port 5000.
Routes:
/states: Generates an HTML page featuring a list of all State objects.
/states/<id>: Creates an HTML page showcasing the specified state with <id>.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Shows an HTML page presenting a list of all states,
    sorted alphabetically by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
Shows an HTML page with information about <id> if it is present."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """
Removes the existing SQLAlchemy session.."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
