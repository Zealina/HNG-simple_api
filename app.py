#!/usr/bin/env python3
"""Simple API to return Basic credentials"""

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Returns owner credentials"""
    my_credentials_json = {
            'email': 'hamilsebastine@gmail.com',
            'current_datetime': datetime.utcnow().isoformat() + 'Z',
            'github_url': 'https://github.com/Zealina/HNG-simple_api'
            }
    return (jsonify(my_credentials_json)), 200


if __name__ == '__main__':
    app.run(port=5000)
