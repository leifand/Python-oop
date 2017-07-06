'''
    portfolio.py
    Leif Anderson 7/6/17
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainPage():
  return render_template('portfolio_main.html')

@app.route('/projects')
def projectsPage():
    return render_template('portfolio_projects.html')

@app.route('/about')
def aboutPage():
    return render_template('portfolio_about.html')

app.run(debug=True)
