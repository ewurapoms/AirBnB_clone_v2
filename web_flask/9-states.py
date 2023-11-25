#!/usr/bin/python3
"""Start a Flask web application:States and State"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """shows an HTML page that lists all states & cities"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """shows an HTML page that lists all states & cities"""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)

    return render_template('states.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """prints an HTML about <id>, where existing"""
    state = storage.get(State, id)

    if state:
        c_sorted = sorted(state.cities, key=lambda s: s.name)
        return render_template('9-states.html', state=state, cities=c_sorted)
    else:
        return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
