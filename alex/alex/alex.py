# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, request, jsonify
from flask_mail import Message, Mail
app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'alex.db'),
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
	
))
app.config.from_envvar('alex_SETTINGS', silent=True)

app.config.update(
	
		#EMAIL SETTINGS
		MAIL_SERVER='email-smtp.us-east-1.amazonaws.com',
		MAIL_PORT=465,
		MAIL_USE_SSL=True,
		MAIL_USE_TLS=False,
		MAIL_USERNAME='AKIAJQD3DQBN6Q677DUQ',
		MAIL_PASSWORD='Ai6mnfN0JxYMD9akF0y8s9PhMmP+woi9hd4AHMpyHHMU'

)
mail=Mail(app)

def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv
	
def init_db():
	"""Initializes the database."""
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()


@app.cli.command('initdb')
def initdb_command():
	"""Creates the database tables."""
	init_db()
	print('Initialized the database.')


def get_db():
	"""Opens a new database connection if there is none yet for the
	current application context.
	"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
	"""Closes the database again at the end of the request."""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


@app.route('/', methods=['GET', 'POST'])
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
	fname=request.form['first_name']
	lname=request.form['last_name']
	email=request.form['email']
	phone=request.form['phone']
	addy=request.form['address']
	state=request.form['state']
	message=request.form['comment']

	
	
  
	msg = Message('Hello', sender = 'lexloulou@gmail.com', recipients = ['lexloulou@gmail.com'])
	msg.body = "Hello Flask message sent from Flask-Mail"
	msg.html = render_template('form.html', name=fname, lastname=lname, email=email, phone=phone,address=addy,state=state,message=message)
	mail.send(msg)
	return "Sent"

if __name__ == '__alex__':
	app.run(debug=True)

   
