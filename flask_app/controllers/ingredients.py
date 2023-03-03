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
    return render_template("new_ingredient.html")

@app.route("/ingredients/save_to_db", methods=['POST'])
def save_ingredient_to_db(): 
    
    user_supplied_form_data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "user_id": session['user_id']
    } 
    valid_ingredient = Ingredient.save_valid_ingredient(user_supplied_form_data)
    if not valid_ingredient:
        print("   *!*!*!*!*!*!*   CREATE FAILED   *!*!*!*!*!*!*   ")
        return redirect("/ingredients/new")
    print("   *$*$*$*$*$*$*   INGREDIENT POSTED SUCCESSFULLY    *$*$*$*$*$*$*   ")
    return redirect('/ingredients/list')

@app.route('/ingredients/edit/<int:ingredient_id>')
def edit_ingredient_page(ingredient_id):
    if 'user_id' not in session:
        print("   *!!!*!!!*!!!*   ACCESS DENIED - NOT IN SESSION   *!!!*!!!*!!!*   ")
        return redirect('/')
    ingredient_data ={"id":ingredient_id}
    return render_template("edit_ingredient.html" , ingredient=Ingredient.get_one_ingredient(ingredient_data) , user = user.User.get_by_id(session['user_id']) )
