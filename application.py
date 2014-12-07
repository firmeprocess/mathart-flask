import os

# SET UP ENVIRONMENT
from common_functions import read_env, env_var
read_env()

# FLASK
from flask import Flask
from flask import render_template



app = Flask(__name__)

if env_var('ENVIRONMENT') == 'LOCAL':
    app.debug=True

@app.route('/')
def hello():
    return render_template('hello_world.html', message="hello world")


