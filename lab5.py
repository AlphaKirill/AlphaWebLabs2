from flask import redirect, render_template, request, Blueprint
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

    print(result)

    dbClose(cur, conn)

    return "go to console"


@lab5.route('/lab5/users')
def adding():
    global global_result

    len_res = len(global_result)
    return render_template('users.html', result=global_result, len_res=len_res)
    
