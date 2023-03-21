from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user, upcoming, review
from flask_app.controllers import users_control

@app.route('/')
def dashboard():
    if "user_id" in session:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        upcoming_list = upcoming.Upcoming.get_all_upcoming()
        new_reviews = review.Review.top_reviews()
        return render_template('dashboard.html',user = user_info, games= upcoming_list, new = new_reviews)
    upcoming_list = upcoming.Upcoming.get_all_upcoming()
    new_reviews = review.Review.top_reviews()
    return render_template('dashboard.html', games = upcoming_list,new = new_reviews)

@app.route('/review_form')
def review_form():
    if "user_id" in session and session["user_id"] == 1:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        return render_template('add_review.html', user = user_info)
    return redirect('/')

@app.route('/add_review', methods=['POST'])
def add_review():
    data = {
        "user_id" : session['user_id'],
        'title' : request.form['title'],
        'image' : request.form['image'],
        'score' : request.form['score'],
        'description' : request.form['description'],
        'joys' : request.form['joys'],
        'no_joys' : request.form['no_joys']
    }
    if "user_id" not in session or session["user_id"] != 1:
        return redirect('/')
    if "user_id" in session and session["user_id"] == 1:
        if review.Review.add_review(data):
            return redirect('/')
    return redirect('/review_form')

@app.route('/all_reviews')
def all_reviews():
    if "user_id" in session:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        review_list = review.Review.all_reviews()
        return render_template('all_reviews.html', user = user_info, review = review_list)
    review_list = review.Review.all_reviews()
    return render_template('all_reviews.html', review = review_list)

@app.route('/edit_review/<int:id>')
def edit_review(id):
    if "user_id" in session and session['user_id'] == 1:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        one_review = review.Review.review_by_id({'id' : id})
        return render_template('edit_review.html', user = user_info, review = one_review)
    return redirect('/')

@app.route('/process_edit/<int:id>', methods=['POST'])
def process_edit(id):
    if "user_id" in session and session['user_id'] == 1:
        data = {
            'id' : id,
            'title': request.form['title'],
            'image' : request.form['image'],
            'score' : request.form['score'],
            'description' : request.form['description'],
            'joys' : request.form['joys'],
            'no_joys': request.form['no_joys']
        }
        if review.Review.edit_review(data):
            return redirect(f'/one_review/{id}')
        return render_template(f'/edit_review/{id}')
    return redirect('/')

@app.route('/delete_review/<int:id>')
def delete_review(id):
    if "user_id" in session and session['user_id'] == 1:
        review.Review.delete_review({'id' : id})
        return redirect('/all_reviews')
    return redirect('/')

@app.route('/one_review/<int:id>')
def one_review(id):
    if "user_id" in session:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        one_review = review.Review.review_by_id({'id' : id})
        return render_template('one_review.html', user = user_info, review = one_review)
    one_review = review.Review.review_by_id({'id' : id})
    return render_template('one_review.html', review = one_review)

@app.route('/upcoming')
def upcoming_form():
    if "user_id" in session and session['user_id'] == 1:
        user_info = user.User.get_user_id({'id' : session['user_id']})
        return render_template('upcoming.html', user = user_info)
    return redirect('/')

@app.route('/upload', methods=['POST'])
def upload_upcoming():
    data = {
        'image' : request.form['image'],
        'user_id' : session['user_id']
    }
    if upcoming.Upcoming.add_upcoming(data):
        return redirect('/')
    return redirect('/upcoming')

@app.route('/delete_upload/<int:id>')
def delete_upcoming(id):
    upcoming.Upcoming.delete_upcoming({'id' : id})
    return redirect('/')