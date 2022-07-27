from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Lour"
password = "Meet2022"
facebook_friends=["Paulina","Noam","Yasmin", "Lian", "Mayar"]



@app.route('/', methods = ["GET", "POST"])  # '/' for the default page
def login():
  if request.method == 'GET':
    return render_template('form.html')
  else:
    username = request.form['username']
    password = request.form['password']
    return render_template('home.html',friends=facebook_friends)

@app.route ('/friend_exists/<string:name>')
def friend_exists(name):
	return render_template('friend_exists.html')







if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)