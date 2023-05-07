#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, renter_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display 'C' followed by 'text'"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python/(<text>)', strict_slashes=False)
def pythoniscool(text='is cool'):
    """displays 'Python' followed by <text>"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<n>', strict_slashes=False)
def isanumber(n):
    return "{:d} is a number".format(n)

@app.route('number/<int:n>', strict_slashes=False)
def numbersandtemplate(n):
    """displays a HTML page if n is an interger"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
