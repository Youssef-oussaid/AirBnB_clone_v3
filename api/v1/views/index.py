#!/usr/bin/python3
"""returns the status in a json form"""

from flask import jsonify
from api.v1.views import app_views, storage


@app_views.route('/status')
def status():
    """return api status"""
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    pass