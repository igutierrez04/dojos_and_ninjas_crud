from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
def index():
    return redirect('/dojo')

@app.route('/dojo')
def dojo():
    return render_template('dojo.html', dojos = Dojo.get_all_dojos())


@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['dojo_name']
    }
    Dojo.create_dojo(data)
    return redirect('/dojo')

@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    data = {
        'id': id
    }
    return render_template('show_dojo.html', dojo_data = Dojo.get_dojo_w_ninjas(data))