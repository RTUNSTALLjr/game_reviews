from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user, upcoming, comment
from flask import flash, session
import re 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

db = 'reviews_db'

class Review:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.image = data['image']
        self.score = data['score']
        self.description = data['description']
        self.joys = data['joys']
        self.no_joys = data['no_joys']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comments = []

    @classmethod
    def add_review(cls, data):
        if not cls.validate_review(data):
            return False
        query = """
        INSERT INTO reviews (title, image, score, description, joys, no_joys, user_id)
        VALUES (%(title)s,%(image)s,%(score)s,%(description)s,%(joys)s,%(no_joys)s,%(user_id)s )
        ;"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def edit_review(cls, data):
        if not cls.validate_review(data):
            return False
        query = """
        UPDATE reviews
        SET title = %(title)s, image = %(image)s, score = %(score)s, description = %(description)s, joys = %(joys)s, no_joys = %(no_joys)s
        WHERE id = %(id)s
        ;"""
        connectToMySQL(db).query_db(query, data)
        return True

    @classmethod
    def all_reviews(cls):
        query = """
        SELECT * FROM reviews
        ;"""
        results = connectToMySQL(db).query_db(query)
        review_list = []
        for row in results:
            review = cls(row)
            review_list.append(review)
        return review_list

    @classmethod
    def review_by_id(cls, data):
        query = """
        SELECT * FROM reviews
        WHERE reviews.id = %(id)s
        ;"""
        results = connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_review(data):
        is_valid = True
        if len(data['title']) < 1:
            flash('Title is required.', 'title')
            is_valid = False
        if len(data['image']) < 1:
            flash('Image is required.', 'review_image')
            is_valid = False
        if len(data['score']) < 1:
            flash('Score is required.', 'score')
            is_valid = False
        if len(data['score']) > 5:
            flash('Score must be between 1 and 5.', 'score')
            is_valid = False
        if len(data['description']) < 1:
            flash('Description is required.', 'review')
            is_valid = False
        if len(data['joys']) < 1:
            flash('Joys is required.', 'joys')
            is_valid = False
        if len(data['no_joys']) < 1:
            flash('No Joys is required.', 'no_joys')
            is_valid = False
        return is_valid
    
