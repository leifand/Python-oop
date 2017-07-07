'''
    server.py
    Landing Page Exercise
    Leif Anderson 7/7/17
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def new_ninja():
    return render_template('dojo.html')

# Run, server, run!
app.run(debug=True)
