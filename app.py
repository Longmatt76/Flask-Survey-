from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app= Flask(__name__)
app.config["SECRET_KEY"] = "buster"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)





@app.route('/')
def show_home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', survey_title= title, survey_instructions= instructions )

@app.route('/set_session', methods=["POST"])
def set_session():
    session["responses"] = []
    return redirect('question/0')


@app.route('/question/<int:idx>')
def show_question(idx):
    if len(session["responses"]) == len(satisfaction_survey.questions):
         return redirect('/thank_you')
    
    if len(session["responses"]) != idx:
          flash("You cannot access questions out of order")
          return redirect(f'/question/{len(session["responses"])}')
    else:
        question = satisfaction_survey.questions[idx]
        return render_template('question.html', survey_question= question)


@app.route('/answer',methods =["POST"])
def log_answer():
    response = request.form["answer"]
    responses = session["responses"]
    responses.append(response)
    session["responses"] = responses

    if len(responses) == len(satisfaction_survey.questions):
         return redirect('/thank_you')
    else:
         return redirect(f'/question/{len(responses)}')
    


@app.route('/thank_you')
def say_thanks():
    return render_template("thanks.html")