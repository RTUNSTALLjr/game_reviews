from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import review, user, comment
from flask import flash, session
import re 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

db = 'reviews_db'

class Upcoming:
    def __init__(self, data):
        self.id = data['id']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_upcoming(cls):
        query = """
        SELECT * FROM upcoming
        LIMIT 2
        ;"""
        results = connectToMySQL(db).query_db(query)
        upcoming_list = []
        for row in results:
            upcoming = cls(row)
            upcoming_list.append(upcoming)
        return upcoming_list
    
    @classmethod
    def add_upcoming(cls, data):
        if not cls.validate_upcoming(data):
            return False
        query ="""
        INSERT INTO upcoming (image, user_id)
        VALUES (%(image)s, %(user_id)s)
        ;"""
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def delete_upcoming(cls, data):
        query = """
        DELETE FROM upcoming
        WHERE id = %(id)s
        ;"""
        connectToMySQL(db).query_db(query, data)
    
    @staticmethod
    def validate_upcoming(data):
        is_valid = True
        if len(data['image']) < 1:
            flash("Image is required", "upcoming")
            is_valid = False
        return is_valid