#####################################
#
#   imports(s)
#
#####################################


from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash



#####################################
#
#   global variable(s)
#
#####################################


DB = "myPantry"



#####################################
#
#   Ingredient class
#
#####################################


class Ingredient:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']



#####################################
#
#   @class method(s)
#
#####################################


    @classmethod
    def get_all_ingredients(cls):
        query = "SELECT * FROM ingredients;"
        results = connectToMySQL(DB).query_db(query)
        ingredients_list = []
        for ingredients_dictionary in results:
            ingredients_class = cls(ingredients_dictionary)
            ingredients_list.append(ingredients_class)
        print(ingredients_list)
        return ingredients_list
    
    @classmethod
    def get_all(cls):
        query = "select * from users";
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        print(users)
        return users
    
    @classmethod
    def get_all_shows_with_poster_data(cls):
        query = "SELECT * FROM shows JOIN users on shows.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        show_list = []
        for show_user_dictionary in results:
            show_class = cls(show_user_dictionary)
            show_list.append(show_class)
        return show_list
        
        

#####################################
#
#   @static method(s)            
#
#####################################


    @staticmethod
    def is_valid(ingredient):
        valid = True
        if len(ingredient["name"]) < 3:
            valid = False
            flash("Name must be at least 3 characters.", "ingredient")           
        if len(ingredient["description"]) < 3:
            valid = False
            flash("Description must be at least 3 characters.", "ingredient") 
        return valid
