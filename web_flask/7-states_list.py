#!/usr/bin/python3
"""
starts Flask application
"""


from flask import Flask, render_template
from models import *
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays a HTML page with the states listed in alpabetical order"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    print(state)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
