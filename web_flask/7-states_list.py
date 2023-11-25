#!/usr/bin/python3
"""Start a Flask web application:state list"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """prints an HTML page that lists all states"""
    states = storage.all(State).values()
    newStates = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=newStates)


@app.teardown_appcontext
def db_teardown(self):
    """ends any current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
