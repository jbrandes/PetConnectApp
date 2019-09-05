import flask
from flask import Flask, redirect, url_for, render_template, request
import petpy
import os
from app import app


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/location', methods = ['POST'])
def location():
    location = request.form['location']
    return render_template('home.html')


@app.route('/animal', methods = ['POST'])
def animal():
    animal = request.form['animal']
    return render_template('home.html')
    


if __name__ == "__main__":
    app.run(debug=True)
