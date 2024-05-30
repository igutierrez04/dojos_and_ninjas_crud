from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja

class Dojo:
    # variable to store the name of the database we are connecting to
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Create an empty list to store ninjas associated with the dojos
        self.ninjas = []


    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
    

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        # empty list to store dojos
        dojos = []
        # for loop to iterate over the db results and create an instance of each dojo
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_dojo_w_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)

        dojo = cls(results[0])
        for db_info in results:
            ninja_data = {
                "id": db_info["ninjas.id"],
                "first_name": db_info["first_name"],
                "last_name": db_info["last_name"],
                "age": db_info["age"],
                "created_at": db_info["created_at"],
                "updated_at": db_info["updated_at"],
                "dojo_id": db_info["dojo_id"]
            }
            dojo.ninjas.append( Ninja( ninja_data ))
        return dojo