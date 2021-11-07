# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_survey import Survey

@app.route('/')
def survey():
    return render_template('survey.html')

