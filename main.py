from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app import app, db
from app import forms
from app.models import User
from app.forms import LoginForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        pwd = request.form["password"]

        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or user.verify_password(pwd):
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html', form=forms)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run(debug=True)