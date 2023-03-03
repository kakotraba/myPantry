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
    def save_valid_ingredient(cls, request_form_data):
        if not cls.is_valid(request_form_data):
            print("   *!*!*!*!*!*!*   INVALID INGREDIENT DATA   *!*!*!*!*!*!*   ")
            return False
        print("   *$*$*$*$*$*$*   INGREDIENT DATA VALIDATED    *$*$*$*$*$*$*   ")
        query = """INSERT INTO ingredients (name , description)
                    VALUES (%(name)s, %(description)s)
                    """
        result = connectToMySQL(DB).query_db(query, request_form_data)
        return result
        
    @classmethod
    def get_one_ingredient(cls,ingredient_id):
        query = "SELECT * FROM ingredients WHERE ingredients.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,ingredient_id)
        #print(result[0])
        ingredient_class = cls(result[0])
        print(ingredient_class)
        return ingredient_class
    
    @classmethod
    def delete(cls,ingredient_id):
        query = "DELETE FROM ingredients WHERE id = %(id)s"
        result = connectToMySQL(DB).query_db(query,ingredient_id)
        print(result)

        

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
