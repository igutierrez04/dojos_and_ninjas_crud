from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/ninja/create')
def ninja():
    return render_template('create_ninja.html', dojos = Dojo.get_all_dojos())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    return redirect('/dojo/show')