
#####################################
#
#   import(s)
#
#####################################


from flask import redirect,render_template,request,session
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.ingredient import Ingredient
from flask_app.models.user import User



#####################################
#
#   @app.route(s)
#
#####################################



@app.route('/recipes/list')
def list_recipes():
    if 'user_id' not in session:
        print("   *!!!*!!!*!!!*   ACCESS DENIED - NOT IN SESSION   *!!!*!!!*!!!*   ")
        return redirect('/')
    return render_template("list_recipes.html" , user = User.get_by_id(session['user_id']) , recipe_list = Recipe.get_all_recipes_with_ingredients())

#new_recipe_page...render a page to enter new recipe data into a form
@app.route('/recipes/new')
def new_recipe_page():
    if 'user_id' not in session:
        print("   *!!!*!!!*!!!*   ACCESS DENIED - NOT IN SESSION   *!!!*!!!*!!!*   ")
        return redirect('/')
    return render_template("new_recipe.html" , ingredient_list = Ingredient.get_all_ingredients())


#save_recipe_to_db...parse form data into dictionary, run a classmethod to validate the entered data and save to the DB
@app.route("/recipes/save_to_db", methods=['POST'])
def save_recipe_to_db(): 
    
    user_supplied_form_data = {
        "name": request.form['name'],
        "instructions": request.form['instructions'],
        "ingredient_1": request.form['ingredient_1'],
        "ingredient_2": request.form['ingredient_2'],
        "ingredient_3": request.form['ingredient_3'],
        "user_id": session['user_id']
    } 
    valid_recipe = Recipe.save_valid_recipe(user_supplied_form_data)
    if not valid_recipe:
        print("   *!*!*!*!*!*!*   CREATE FAILED   *!*!*!*!*!*!*   ")
        return redirect("/recipes/new")
    print("   *$*$*$*$*$*$*   RECIPE POSTED SUCCESSFULLY    *$*$*$*$*$*$*   ")
    return redirect('/recipes/list')