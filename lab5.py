from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, Blueprint, session, url_for
import psycopg2


lab5 = Blueprint('lab5',__name__)

global_result = []

def dbConnect():
    # Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_kirill", user="kirill_knowledge_base",
        password="chel")
    
    return conn

def dbClose(cursor, connection):
    # Закрываем соединение с БД
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():
    
    conn = dbConnect()
    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы cur = conn.cursor()
    cur = conn.cursor()

    # Пишем запрос, который psycopg2 должен выполнить
    cur.execute("SELECT * FROM users;")

    # fetchall
    # выполнения SQL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()

    global global_result
    global_result = result

    username = session.get('username', 'Anon')
    dbClose(cur, conn)

    if not username:
        visibleUser = 'Anon'
    else:
        visibleUser = username

    return render_template('laba5.html', username=visibleUser, result=result)


@lab5.route('/lab5/users')
def adding():
    global global_result
    
    len_res = len(global_result)
    return render_template('users.html', result=global_result, len_res=len_res)

@lab5.route('/lab5/register', methods=["GET", "POST"]) 
def registerPage(): 
    errors = [] 

    if request.method == 'GET':
        return render_template("register.html", errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)

    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{ username }';")

    resultСur = cur.fetchone()

    if resultСur != None:
        errors.append('Пользователь с данным именем уже существует')

        dbClose(cur, conn)

        return render_template('register.html', errors=errors, resultСur=resultСur)

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashPassword}');")

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login")


@lab5.route('/lab5/login', methods=["GET", "POST"])
def loginPage():

    errors = []

    if request.method == 'GET':
        return render_template('login.html', errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")
    
    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        return render_template("login.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute(f"SELECT id, password FROM users WHERE username = '{ username }'")
    result = cur.fetchone()

    if result is None:
        errors.append('Неправильный пользователь или пароль')
        dbClose(cur, conn)
        return render_template("login.html", errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5")
    else:
        errors.append("Неправильный логин или пароль")
        return render_template("login.html", errors=errors)
    

@lab5.route("/lab5/new_article", methods=["GET", "POST"])
def createArticle():
    errors = []

    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html")

        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(text_article) == 0:
                errors.append("Заполните текст")
                return render_template("new_article.html", errors=errors)

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles(user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id", (userID, title, text_article))

            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_article_id}")

    return redirect("/lab5/login")


@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"

        text = articleBody[1].splitlines()

        return render_template("ArticleShow.html", article_text=text, article_title=articleBody[0], username=session.get("username"))



@lab5.route("/lab5/AllShow")
def getTitles():
    userID = session.get("id")
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute(f"SELECT title, id FROM articles WHERE user_id = {userID}")

        articles = cur.fetchall()
        dbClose(cur, conn)
        if not articles:
            return "Not found!"
        return render_template("AllArtShow.html",  article_titles=articles, username=session.get("username"))
    

@lab5.route("/lab5/logout")
def logout():
    session.clear()
    return redirect(url_for("lab5.main"))

    
