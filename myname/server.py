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

@app.route('/process')
def getName():
    pass

# Run, server, run!
app.run(debug=True)
