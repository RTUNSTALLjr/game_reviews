from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user
# from flask_app.controllers import review_control

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/all_reviews')
def all_reviews():
    return render_template('all_reviews.html')

@app.route('/one_review')
def one_review():
    return render_template('one_review.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_user', methods=['POST'])
def login_user():
    if user.User.login(request.form):
        return redirect('/')
    return redirect('/login')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/process', methods=['POST'])
def process_registration():
    if user.User.register(request.form):
        return redirect('/')
    return redirect('/register')