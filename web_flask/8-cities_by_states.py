#!/usr/bin/python3
"""Start a Flask web application:Cities by states"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """ends database session"""
    storage.close()


@app.route('/cities_by_states')
def cities_by_state():
    """shows an HTML page that lists all states & cities"""
    states = storage.all(State).values()
    city_states = sorted(states, key=lambda cs: cs.name)
    return render_template('8-cities_by_states.html', states=city_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
