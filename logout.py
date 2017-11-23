from app import app
from flask import Flask, render_template

#import app is the app configuration
#import flask is the flask frameework.

@app.route('/api/auth/<id>/logout', methods = ['POST']) #logout a specific user with id  
def logout_user(id):
return render_template('logout.html')


