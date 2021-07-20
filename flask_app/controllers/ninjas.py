from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos = dojos)

@app.route('/dojos/create', methods = ['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.get_dojo(data)
    return render_template('dojo.html', dojo = dojo)

@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('ninja.html', dojos = dojos)


@app.route('/ninjas/create', methods = ['POST'])
def create_ninja():
    ninja = Ninja.create_ninja(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojos/{dojo_id}')