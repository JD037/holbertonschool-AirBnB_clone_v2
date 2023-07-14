#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


def StartFlask():
    """ Start a Flask web application """
    app.run(host='0.0.0.0', port=5000)


@app.route('/states_list')
def states_list():
    """Display a HTML page with a list of all states"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    StartFlask()
