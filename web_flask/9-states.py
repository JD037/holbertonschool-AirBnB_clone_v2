#!/usr/bin/python3
"""
Script that starts a Flask web application to list states and individual states
"""

from flask import Flask, render_template
from models import storage

# create an instance of the Flask class
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Fetches all State objects and serves them in a template"""
    states = storage.all('State').values()  # fetch all states
    states = sorted(states, key=lambda state: state.name)  # sort states by name
    return render_template('9-states.html', states=states)  # render template with states


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Fetches a State object by ID and serves it in a template"""
    states = storage.all('State')  # fetch all states
    state = states.get('State.' + id)  # get state by id
    return render_template('9-states.html', state=state)  # render template with the state


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()  # close storage


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # run the Flask application
