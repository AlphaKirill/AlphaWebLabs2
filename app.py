from flask import Flask, redirect
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

    <a href="/lab1" target="_blank">Лабараторная работа 1</a>

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

    <footer>
        &copy; Кирилл Белкин, ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>

"""