from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)

@lab1.route('/')
@lab1.route('/index')
def start():
    return redirect("/menu", code=302)


@lab1.route('/menu')
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
    <a href="/lab2" target="_blank">Лабараторная работа 2</a><br>
    <a href="/lab3/" target="_blank">Лабараторная работа 3</a><br>
    <a href="/lab4/" target="_blank">Лабараторная работа 4</a><br>
    <a href="/lab5/" target="_blank">Лабараторная работа 5</a><br>
    <a href="/lab6/" target="_blank">Лабараторная работа 6</a><br>
    <a href="/lab7/" target="_blank">Лабараторная работа 7</a><br>
    <a href="/lab8/" target="_blank">Лабараторная работа 8</a><br>
    <a href="/lab9/" target="_blank">Лабараторная работа 9</a><br>

    <footer>
        &copy; Кирилл Белкин, ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>

"""


@lab1.route('/lab1')
def lab():
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


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
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


@lab1.route('/lab1/python')
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


@lab1.route('/lab1/ds3')
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