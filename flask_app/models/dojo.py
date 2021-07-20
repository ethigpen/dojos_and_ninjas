from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(dojo_name)s);"
        new_dojo_id = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return new_dojo_id

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for item in results:
            new_dojo = Dojo(item)
            dojos.append(new_dojo)
        return dojos

    @classmethod
    def get_dojo(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = Dojo(results[0])
        for item in results:
            if item['ninjas.id']!= None:
                ninja_data = {
                    'id': item['ninjas.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'age': item['age'],
                    'created_at': item['ninjas.created_at'],
                    'updated_at': item['ninjas.updated_at'],
                    'dojo_id': item['dojo_id']
                }
                ninja = Ninja(ninja_data)
                ninja.dojo = dojo
                dojo.ninjas.append(ninja)
        return dojo