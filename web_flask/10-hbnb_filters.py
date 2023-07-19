#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all("State").values()
    cities = storage.all("City").values()
    amenities = storage.all("Amenity").values()
    states = sorted(states, key=lambda state: state.name)
    cities = sorted(cities, key=lambda city: city.name)
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
