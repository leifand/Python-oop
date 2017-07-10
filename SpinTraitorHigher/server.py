from flask import Flask, render_template, redirect, request, session
from random import randint
app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def index():
    if 'info' not in session:
        session['info'] = ' '
    if 'wincount' not in session:
        session['wincount'] = 0
    if 'tiecount' not in session:
        session['tiecount'] = 0
    if 'losscount' not in session:
        session['losscount'] = 0
    return render_template('index.html')


@app.route('/process_play', methods=['POST'])
def process_play():
    userchoice = request.form['Button']
    computerchoice = randint(0, 2)
    list = ["Spin Move", "Traitor", "Higher Ground"]
    computerchoice = list[computerchoice]
    if userchoice == "Spin Move" and computerchoice == "Spin Move":
        result = "Stalemate"
        image1 = './static/jpg/spin.jpg'
        image2 = './static/jpg/spin.jpg'
    elif userchoice == "Spin Move" and computerchoice == "Traitor":
        result = "Victory"
        image1 = './static/jpg/spin.jpg'
        image2 = './static/jpg/traitor.jpg'
    elif userchoice == "Spin Move" and computerchoice == "Higher Ground":
        result = "DEFEAT"
        image1 = './static/jpg/spin.jpg'
        image2 = './static/jpg/higher.jpg'
    elif userchoice == "Traitor" and computerchoice == "Spin Move":
        result = "DEFEAT"
        image1 = './static/jpg/traitor.jpg'
        image2 = './static/jpg/spin.jpg'
    elif userchoice == "Traitor" and computerchoice == "Traitor":
        result = "Stalemate"
        image1 = './static/jpg/traitor.jpg'
        image2 = './static/jpg/traitor.jpg'
    elif userchoice == "Traitor" and computerchoice == "Higher Ground":
        result = "Victory"
        image1 = './static/jpg/traitor.jpg'
        image2 = './static/jpg/higher.jpg'
    elif userchoice == "Higher Ground" and computerchoice == "Spin Move":
        result = "Victory"
        image1 = './static/jpg/higher.jpg'
        image2 = './static/jpg/spin.jpg'
    elif userchoice == "Higher Ground" and computerchoice == "Traitor":
        result = "DEFEAT"
        image1 = './static/jpg/higher.jpg'
        image2 = './static/jpg/traitor.jpg'
    elif userchoice == "Higher Ground" and computerchoice == "Higher Ground":
        result = "Stalemate"
        image1 = './static/jpg/higher.jpg'
        image2 = './static/jpg/higher.jpg'
    info = "You chose " + userchoice + \
        " and the computer chose " + computerchoice + "." + "  >>> " + result + " <<<"

    session['image1'] = image1
    session['image2'] = image2
    session['info'] = info
    if result == "Victory":
        session['wincount'] += 1
    if result == "Stalemate":
        session['tiecount'] += 1
    if result == "DEFEAT":
        session['losscount'] += 1

    return redirect('/')


app.run(debug=True)
