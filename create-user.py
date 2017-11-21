from app import app
from flask import Flask, render_template

@app.route('/api/auth/register', methods = ['POST'])
def create_account():
    return render_template('create-user.html')