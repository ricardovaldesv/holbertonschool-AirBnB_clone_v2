#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask, render_template
from models import storage
from models.state import State, City

app = Flask(__name__)


@app.teardown_appcontext
def close_database(exc):
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """/states_list route"""
    states_list = list(storage.all(State).values())
    states_list.sort(key=lambda x: x.name)
    return render_template('9-states.html', states=states_list)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """/states_list route"""
    states_list = list(storage.all(State).values())
    states_list = [state for state in states_list if state.id == id]
    city_list = list(storage.all(City).values())
    city_list.sort(key=lambda x: x.name)
    return render_template('9-states.html',
                           states=states_list, cities=city_list, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
