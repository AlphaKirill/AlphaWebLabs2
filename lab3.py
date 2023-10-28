from flask import Blueprint, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab_3():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form_1():
    errors = {}
    errors1 = {}
    user = request.args.get('user')
    age = request.args.get('age')
    if user == '' or age == '':
        errors ['user'] = 'Заполни поле!'
        errors1 ['age'] = 'Заполни поле!'
        
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors, errors1=errors1)