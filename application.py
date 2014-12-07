import os, sys

# SET UP ENVIRONMENT
from common_functions import read_env, env_var
read_env()

# FLASK
from flask import Flask
from flask import render_template

app = Flask(__name__)

if env_var('ENVIRONMENT') == 'LOCAL':
    sys.stdout.write('\033[0;31m  >>  Running on LOCAL environment \033[0;0m\n')
    app.debug=True


### PROFILE ###

@app.route('/')
def home():
    return render_template('hello_world.html', message="Welcome to *")


### SIGNUP ###
@app.route('/profile')
def signup():
    return render_template('signup.html')


### PROFILE ###

@app.route('/profile')
def profile():
    return render_template('profile.html')


### ABOUT ###

@app.route('/about')
def about():
    return render_template('profile.html')


### MATHART ###

@app.route('/mathart')
def mathart():
    return render_template('mathart/mathart.html', message="Welcome to *")

@app.route('/mathart/twitter')
def mathart_twitter():
    return render_template('mathart/mathart_twitter.html', message="Welcome to *")

@app.route('/mathart/instagram')
def mathart_instagram():
    return render_template('mathart/mathart_instagram.html', message="Welcome to *")

