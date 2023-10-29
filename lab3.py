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


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def ticket():
    errorst = {}
    errorst1 = {}
    usert = request.args.get('usert')
    aget = request.args.get('aget')
    bag = request.args.get('bag')
    travel = request.args.get('travel')
    transit = request.args.get('transit')
    DATA = request.args.get('DATA')

    if usert == '':
        errorst ['usert'] = 'Заполни поле!'
    if aget == '':
        errorst ['aget'] = 'Заполни поле!'
    if transit == '':
        errorst ['transit'] = 'Заполни поле!'
    if travel == '':
        errorst ['travel'] = 'Заполни поле!'
    if DATA == '':
        errorst ['DATA'] = 'Заполни поле!'
    
    if request.args.get('bag') == 'on':
        bag = 'Да'
    else:
        bag = 'Нет'
    
    typet = request.args.get('typet')
    site = request.args.get('site')
    return render_template('ticket.html', usert=usert, aget=aget, typet=typet, site=site, bag=bag, travel=travel,
                           transit=transit,DATA=DATA, errorst=errorst, errorst1=errorst1)