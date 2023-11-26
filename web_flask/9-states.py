#!/usr/bin/python3
"""Start a Flask web application:Cities by states"""

from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states_by_state():
    """shows an HTML page that lists all states """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>")
def states_id(id):
    """ shows an HTML page with info about <id>, if it exists """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(self):
    """ends database session"""
    storage.close()


if __name__ == "__main__":
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
