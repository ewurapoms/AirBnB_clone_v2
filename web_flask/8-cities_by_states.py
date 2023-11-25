#!/usr/bin/python3
"""Start a Flask web application:Cities by states"""

from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_state():
    """shows an HTML page that lists all states & cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """ends database session"""
    storage.close()


if __name__ == "__main__":
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
