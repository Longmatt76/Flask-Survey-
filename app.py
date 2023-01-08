from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app= Flask(__name__)
app.config["SECRECT_KEY"] = "buster"

responses = []


@app.route('/')
def show_home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', survey_title= title, survey_instructions= instructions )