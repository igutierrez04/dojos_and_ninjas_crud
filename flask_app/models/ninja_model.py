from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)