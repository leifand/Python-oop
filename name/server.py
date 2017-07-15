'''
    server.py
    What's My Name Exercise
    Leif Anderson 7/12/17
'''
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")

  '''@app.route('/users', methods=['POST'])
  def create_user():
     print "Got Post Info"
     # we'll talk about the following two lines after we learn a little more
     # about forms
     name = request.form['name']
     email = request.form['email']
     print request.form
     # redirects back to the '/' route
     return redirect('/')'''

  @app.route('/users/<username>')
  def show_user_profile(username):
  	print username
      return render_template("user.html")

  app.run(debug=True)
