# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_survey import Survey

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/create', methods=['POST'])
def create_survey():
    session['name'] = request.form['name']
    session['location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comments'] = request.form['comments']
    print(session['name'])
    return redirect('/survey_results')

@app.route('/survey_results')
def display_results():
    return render_template('survey_results.html')
