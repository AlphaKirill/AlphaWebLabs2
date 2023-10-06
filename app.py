from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def start():
    return redirect("/menu", code=302)

@app.route('/menu')
def menu():
    return """

<!DOCTYPE html>
<head>
    <title>НГТУ, ФБ, Лабораторные работы</title>
</head>
<body>
    <header>
       НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
    </header>

    <a href="/lab1" target="_blank">Лабараторная работа 1</a><br>
    <a href="/lab2/example" target="_blank">Лабараторная работа 2</a>

    <footer>
        &copy; Кирилл Белкин, ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>

"""

@app.route('/lab1')
def lab1():
    return """

<!DOCTYPE html>
<head>
    <title>Белкин Кирилл Витальевич, Лабараторная 1</title>
</head>
<body>
    <header>
        НГТУ, ФБ, Лабараторная работа 1
    </header>

    <h1>web-сервер на flask</h1>

    <h2>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
    </h2>

    <a href="/" target="_blank">Меню</a>

    <h3>Реализованные роуты:</h3>
        <a href="/lab1/oak" target="_blank">Дуб</a><br>
        <a href="/lab1/student" target="_blank">Студент</a><br>
        <a href="/lab1/python" target="_blank">Python</a><br>
        <a href="/lab1/ds3" target="_blank">Третий курс</a><br>

    <footer>
        &copy; Кирилл Белкин, ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>

"""

@app.route('/lab1/oak')
def oak():
    return '''

<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''" 
    <title>Белкин Кирилл Витальевич, Лабараторная 1</title>
</head>
<body class="body">
    <header>
        
    </header>

    <h1>Дуб</h1>
    <img class="img_lab1" src="''' + url_for('static', filename='oak.jpg') + '''">

    <footer>
        &copy; Кирилл Белкин, ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>

'''

@app.route('/lab1/student')
def student():
    return '''

<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''" 
    <title>Белкин Кирилл Витальевич, Лабараторная 1</title>
</head>
<body class="body">
    <header>
        
    </header>

    <h1 class="name">Белкин Кирилл Витальевич</h1>
    <img class="img2_lab1" src="''' + url_for('static', filename='nstuPNG.jpg') + '''">

    <footer>
        &copy; Кирилл Белкин, ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>

'''

@app.route('/lab1/python')
def python():
    return '''

<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''" 
    <title>Белкин Кирилл Витальевич, Лабараторная 1</title>
</head>
<body class="body">
    <header>
        
    </header>

    <h1 class="text_programming">
    Python содержит такие структуры данных как списки (lists), кортежи (tuples)<br> 
    и словари (dictionaries). Списки — похожи на одномерные массивы (но вы можете использовать<br> 
    Список включающий списки — многомерный массив), кортежи — неизменяемые списки, словари — тоже списки,<br>
    но индексы могут быть любого типа, а не только числовыми. "Массивы" в Python могут содержать данные любого типа,<br> 
    то есть в одном массиве может могут находиться числовые, строковые и другие типы данных.<br> 
    Массивы начинаются с индекса 0, а последний элемент можно получить по индексу -1<br>
    Вы можете присваивать переменным функции и использовать их соответственно.
    </h1>

    <img class="img3_lab1" src="''' + url_for('static', filename='programming.jpg') + '''">

    <footer>
        &copy; Кирилл Белкин, ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>

'''

@app.route('/lab1/ds3')
def ds3():
    return '''

<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''" 
    <title>Белкин Кирилл Витальевич, Лабараторная 1</title>
</head>
<body class="body">
    <header>
        
    </header>

    <img class="img2_lab1" src="''' + url_for('static', filename='NuKavo.jpg') + '''">
    <h1 class="name">Белкин Кирилл Витальевич на 3ем курсе(3 часть обучения сравнится с 3 частью Dark souls)</h1>
    <h2 class="Nenado">
    Третий курс кажется мне периодом, когда студенты сталкиваются с сложностями сравнинимыми с босс-файтом "Мидир",<br> 
    учебно-практические работы и долгожданные "обновления" от разработчиков НГТУ , которые требуют времени и усилий, а также дают понять,<br> 
    что большую часть времени нужно будет тратить на изучение "механик боя" с дисциплинами, но связи с тем, что две части я уже прошел - навык остался,<br>
    но 3ая часть обучения дает понять, что все же даже данных мне "навыков" за первые 2части обучения может не хватать, поэтому придется<br>
    переосмыслить и переработать свой подход в прохождении данных "серий обучения" для улучшения различных скиллов "выживания"<br>
    в этой не простой серии "НГТУ очное обучение".
    </h2>

    <footer>
        &copy; Кирилл Белкин, ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>

'''

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