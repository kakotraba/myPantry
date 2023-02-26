from flask import redirect,render_template,request

from flask_app import app
from flask_app.models.**MODEL** import **MODEL**

@app.route('/')
def index():
    return render_template('index.html')

