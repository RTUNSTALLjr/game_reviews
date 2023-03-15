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