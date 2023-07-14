#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C' followed by the value of the <text> variable"""
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Display 'Python ', followed by the value of the <text> variable"""
    text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display 'n is a number' only if n is an integer"""
    return '%d is a number' % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
