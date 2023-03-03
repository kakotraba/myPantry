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


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.instructions = data['instructions']
 


#####################################
#
#   @class method(s)
#
#####################################


    @classmethod
    def get_all_recipes_with_ingredients(cls):
        query = """
            SELECT * FROM recipes 
            JOIN recipes_ingredients ON recipes.id = recipes_ingredients.recipes_id 
            JOIN ingredients ON ingredients.id = recipes_ingredients.ingredients_id;
            """
        results = connectToMySQL(DB).query_db(query)
        recipe_list = []
        for recipe_dictionary in results:
            recipe_class = cls(recipe_dictionary)
            recipe_list.append(recipe_class)
        return recipe_list
        
        
    @classmethod
    def save_valid_recipe(cls, request_form_data):
        if not cls.is_valid(request_form_data):
            print("   *!*!*!*!*!*!*   INVALID RECIPE DATA   *!*!*!*!*!*!*   ")
            return False
        print("   *$*$*$*$*$*$*   RECIPE DATA VALIDATED    *$*$*$*$*$*$*   ")
        query = """INSERT INTO recipes (name , instructions)
                    VALUES (%(name)s, %(instructions)s)
                    INSERT INTO recipes_ingredients (recipes_id, ingredients_id)
                    VALUES (%)
                    """
        result = connectToMySQL(DB).query_db(query, request_form_data)
        return result
    
    
    @classmethod
    def get_by_id(cls, recipe_id):
        data = {"id": recipe_id}
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
            print("   *!*!*!*!*!*!*   NO MATCHING USER FOUND   *!*!*!*!*!*!*   ")
        print(cls(result[0]))
        return cls(result[0])
    
    
    
    
    
    
    
    



#####################################
#
#   @static method(s)            
#
#####################################


    @staticmethod
    def is_valid(recipe):
        valid = True
        if len(recipe["name"]) < 3:
            valid = False
            flash("Name must be at least 3 characters.", "recipe")           
        if len(recipe["instructions"]) < 3:
            valid = False
            flash("Instructions must be at least 3 characters.", "recipe") 
        return valid
