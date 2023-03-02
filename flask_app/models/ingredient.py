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
        self.instructions = data['description']



#####################################
#
#   @class method(s)
#
#####################################


    @classmethod
    def get_all_ingredients(cls):
        query = "SELECT * FROM ingedients;"
        results = connectToMySQL(DB).query_db(query)
        ingredient_list = []
        for ingredient_dictionary in results:
            ingredient_class = cls(ingredient_dictionary)
            ingredient_list.append(ingredient_class)
        return ingredient_list
        
        

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
