import flask
from flask import request, redirect
import petpy
import os

@app.route('/')
return render_template('home.html')



@app.route('/location', methods = ['POST'])
def location():
    location = request.form['location']
    return redirect('/')


@app.route('/animal', methods = ['POST'])
def animal():
    animal = request.form['animal']
    return redirect('/')
    

