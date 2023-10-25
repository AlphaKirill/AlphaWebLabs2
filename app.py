from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route('/lab2/example')
def example():
    name = "Белкин К.В."
    lab_number = "Лабараторная 2"
    group = "ФБИ-11"
    kurs = "Курс 3"
    rezylt_1 = 11*8
    rezylt_2 = 8452/793
    rezylt_3 = 45**8
    fruits = [
        {'name':'Яблоки', 'price': 100},
        {'name':'Груши', 'price': 120},
        {'name':'Виноград', 'price': 80},
        {'name':'Мандарины', 'price': 95},
        {'name':'ФейхуА', 'price': 321},
        {'name':'Апельсины', 'price': 123}
    ]
    book = [
        {'autor': 'Роберт Т. Кийосаки', 'genre': 'Предпринимательство, Инвестиции', 'name':'Богатый папа, Бедный папа', 'page': 126},
        {'autor': 'Алекс Лесли', 'genre': 'Общая психология, Соблазнение', 'name':'Жизнь без трусов', 'page': 220},
        {'autor': 'Лев Николаевич Толстой', 'genre': 'Роман', 'name':'Война и мир', 'page': 1117},
        {'autor': 'Фёдор Достоевский', 'genre': 'Роман', 'name':'Преступление и наказание', 'page': 356},
        {'autor': 'Михаил Шолохов', 'genre': 'Рассказ', 'name':'Судьба человека', 'page': 101},
        {'autor': 'Дж. Франзен', 'genre': 'Роман', 'name':'Перекрёстки', 'page': 134},
        {'autor': 'Анна Старобинец', 'genre': 'Роман', 'name':'Лисьи броды', 'page': 87},
        {'autor': 'Фредрик Бакман', 'genre': 'Роман', 'name':'Медвежий угол', 'page': 111},
        {'autor': 'Мария Герус', 'genre': 'Фэнтези-роман', 'name':'Крылья', 'page': 176},
        {'autor': 'Джонатан Свифт', 'genre': 'Роман', 'name':'Путешествия Гулливера', 'page': 202}
    ]
    return render_template('example.html', 
                           name=name, lab_number=lab_number, rezylt_1=rezylt_1, rezylt_2=rezylt_2,rezylt_3=rezylt_3,
                            group=group, kurs=kurs, fruits=fruits, book=book)

@app.route('/lab2')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/oper')
def oper():
    return render_template('oper.html')