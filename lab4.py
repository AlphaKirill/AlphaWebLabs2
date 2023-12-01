from flask import Blueprint, url_for, render_template, request
lab4 = Blueprint('lab4',__name__)


@lab4.route('/lab4/')
def lab_4():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET','POST'])
def login():
    errors = {}
    error = ''
    if request.method == 'GET':
        return render_template('login.html', errors=errors)
    

    username = request.form.get('username')
    password = request.form.get('password')

    if username == '':
        errors['username'] = 'не введен логин'

    if password == '':
        errors['password'] = 'не введен пароль'

    if username == 'alex' and password == '123':
        return render_template('success2.html', username=username)
    
    elif username != '' and password != '':
        error = 'Неверный логин и/или пароль'

    return render_template('login.html', error=error, username=username, password=password, errors=errors)


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():

    errors = {}
    if request.method == 'GET':
        return render_template("fridge.html", errors=errors)
    temp = request.form.get('temp')
    if temp == '':
        errors['temp'] = 'не введена температура'
    if temp:
        temp = int(temp)
        if temp > -1:
            errors['temp'] = 'не удалось установить температуру - слишком высокое значение'
        if -12 < temp < -9:
            errors['temp'] = 'Установлена'
    return render_template("fridge.html", temp=temp, errors=errors)


@lab4.route('/lab4/zernovka', methods=['GET', 'POST'])
def zernovka():
    errors = {}
    if request.method == 'GET':
        return render_template("zernovka.html", errors=errors)
    price = 0
    selected_option = request.form.get('zernovka')
    zerno = ''
    weight = request.form.get('weight')
    if weight:
        weight = int(weight)
        if weight > 500:
            errors['weight3'] = 'Такого объема сейчас нет в наличии'
    if weight == '':
        errors['weight1'] = 'не введен вес'
    if weight <= 0:
        errors['weight2'] = 'неверное значение веса'
    if selected_option == 'ya':
        price += 12500
        zerno = 'ячмень'
    if selected_option == 'ov':
        price += 8500
        zerno = 'овёс'
    if selected_option == 'psh':
        price += 8700
        zerno = 'пшеница'
    if selected_option == 'ro':
        price += 14000
        zerno = 'рожь'
    price = price * weight
    if weight:
        if weight > 50:
            price = price - price * 0.1
    return render_template("zernovka.html", errors=errors,
                           selected_option=selected_option, weight=weight,
                           zerno=zerno, price=price)