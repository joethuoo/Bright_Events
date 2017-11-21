from app import app
from flask import render_template

@app.route('/api/auth/login', methods = ['POST'])
def  login_user():
    return render_template('login.html')
