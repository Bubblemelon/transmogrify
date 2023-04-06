import os
import sys

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# exposes app to the network when `python app.py` initiates
if __name__ == '__main__':
    print('App is running as main!')
    app.run(debug=False, port=5000, host='0.0.0.0')
