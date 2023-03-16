from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash, session
import re 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

db = 'reviews_db'

class Review:
    def __init__(self, data):
        self.title = data['title']
        self.image = data['image']
        self.score = data['score']
        self.description = data['description']
        self.joys = data['joys']
        self.no_joys = data['no_joys']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comments = []