#!/usr/bin/python3
"""Testing documentation of a module
"""
from importlib import import_module
import sys

m_imported = import_module(sys.argv[1])

if m_imported.__doc__ is None:
    print("No module documentation", end="")
else:
    print("OK", end="")

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(self):
    '''
    closes query after each session
    '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    '''
    returns JSON formatted 404 status code response
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
