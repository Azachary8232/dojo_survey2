# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 


class Survey():
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @staticmethod
    def vaildate_info(ninja):
        is_valid = True # we assume this is true
        if len(ninja['name']) < 1: 
            flash("Name must be included.")
            is_valid = False  #-- use different if statement for all inputs
        return is_valid   


    # ***CREATE***

    @classmethod
    def create(cls,data):
        query = "INSERT INTO ninjas (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        ninja_id = connectToMySQL('dojo_survey_schema').query_db(query,data)
        return ninja_id


    # ***Retreive***

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        ninja = connectToMySQL('dojo_survey_schema').query_db(query,data)
        return cls(ninja[0])

    # ***Update***

    # ***Delete***