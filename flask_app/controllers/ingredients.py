#####################################
#
#   import(s)
#
#####################################


from flask import redirect,render_template,request,session
from flask_app import app
from flask_app.models.ingredient import Ingredient
from flask_app.models import user



#####################################
#
#   @app.route(s)
#
#####################################



@app.route('/ingredients/list')
def list_ingredients():
    if 'user_id' not in session:
        print("   *!!!*!!!*!!!*   ACCESS DENIED - NOT IN SESSION   *!!!*!!!*!!!*   ")
        return redirect('/')
    return render_template("list_ingredients.html" , user = user.User.get_by_id(session['user_id']) , ingredient_list = Ingredient.get_all_ingredients())

@app.route('/ingredients/new')
def new_ingredients_page():
    if 'user_id' not in session:
        print("   *!!!*!!!*!!!*   ACCESS DENIED - NOT IN SESSION   *!!!*!!!*!!!*   ")
        return redirect('/')
    return render_template("new_ingredients.html" , ingredient_list = Ingredient.get_all_ingredients)