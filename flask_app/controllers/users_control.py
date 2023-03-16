from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user
# from flask_app.controllers import review_control

@app.route('/')
def dashboard():
    if "user_id" in session:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        return render_template('dashboard.html', user = user_info)
    return render_template('dashboard.html')

@app.route('/all_reviews')
def all_reviews():
    if "user_id" in session:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        return render_template('all_reviews.html', user = user_info)
    return render_template('all_reviews.html')

@app.route('/one_review')
def one_review():
    if "user_id" in session:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        return render_template('one_review.html', user = user_info)
    return render_template('one_review.html')

@app.route('/media')
def media():
    if "user_id" in session:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        return render_template('media.html', user = user_info)
    return render_template('media.html')

@app.route('/login')
def login():
    if "user_id" in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/login_user', methods=['POST'])
def login_user():
    if "user_id" in session:
        return redirect('/')
    if user.User.login(request.form):
        return redirect('/')
    return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register')
def register():
    if "user_id" in session:
        return redirect('/')
    return render_template('register.html')

@app.route('/process', methods=['POST'])
def process_registration():
    if "user_id" in session:
        return redirect('/')
    if user.User.register(request.form):
        return redirect('/')
    return redirect('/register')