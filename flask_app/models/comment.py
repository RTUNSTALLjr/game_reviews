from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user, upcoming, review
from flask import flash, session
import re 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

db = 'reviews_db'

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.score = data['score']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.likes = []

    @classmethod
    def add_comment(cls, data):
        if not cls.validate_comment(data):
            return False
        query = """
        INSERT INTO comments (score, description, user_id, review_id)
        VALUES (%(score)s, %(description)s, %(user_id)s, %(review)s,)
        ;"""
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_comment(data):
        is_valid = True
        if len(data['score']) < 1:
            flash('Score is required.', 'user_score')
            is_valid = False
        if len(data['score']) > 5:
            flash('Score must be between 1 and 5', 'user_score')
            is_valid = False
        if len(data['description']) < 1:
            flash('Description is required.', 'user_description')
            is_valid = False
        return is_valid