from flask import redirect, render_template, request, Blueprint

lab7 = Blueprint('lab7',__name__)


@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')