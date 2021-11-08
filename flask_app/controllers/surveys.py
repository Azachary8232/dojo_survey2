# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_survey import Survey

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/create', methods=['POST'])
def create():
    data = {
        "name" : request.form['name'],
        "location" : request.form['location'],
        "language" : request.form['language'],
        "comment" : request.form['comment']
    }
    print(data)
    id = Survey.create(data)
    return redirect(f'/survey_results/{id}')

@app.route('/survey_results/<int:id>')
def display_results(id):
    data = { 'id' : id }
    ninja = Survey.get_one(data)
    return render_template('survey_results.html', ninja = ninja)
