#!/usr/bin/python3
"""Start a Flask web application: States by State"""

from models import storage
from flask import Flask
from flask import render_template
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """prints HTML page with a list of all states & cities"""
    states = storage.all('State')
    return render_template('9-states.html', state=states)


@app.route('/states/<id>')
def states_id(id):
    """shows an HTML page with info about <id>, if it exists."""
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(self):
    """ends database session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
