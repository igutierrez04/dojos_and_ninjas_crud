from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/ninja/create')
def ninja():
    return render_template('create_ninja.html', dojos = Dojo.get_all_dojos())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect(f'/dojo/show/{request.form["dojo_id"]}')

@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data = {
        'id': id
    }
    return render_template('edit.html', ninja = Ninja.get_one_ninja(data))


@app.route('/ninja/update', methods=['POST'])
def update_ninja():
    print(request.form['dojo_id'])
    Ninja.update_ninja(request.form)
    return redirect(f'/dojo/show/{request.form["dojo_id"]}')

@app.route('/ninja/destroy/<int:ninja_id>/<int:dojo_id>')
def destroy_ninja(ninja_id, dojo_id):
    data = {
        'id': ninja_id
    }
    Ninja.destroy(data)
    return redirect(f'/dojo/show/{dojo_id}')