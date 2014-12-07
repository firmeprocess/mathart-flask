import os, sys

# SET UP ENVIRONMENT
from common_functions import read_env, env_var
read_env()

# FLASK
from flask import Flask
from flask import render_template



app = Flask(__name__)

if env_var('ENVIRONMENT') == 'LOCAL':
    sys.stdout.write('\033[0:31em  >>  Running on LOCAL environment \033[0:0em')
    app.debug=True

@app.route('/')
def home():
    return render_template('hello_world.html', message="Welcome to *")


