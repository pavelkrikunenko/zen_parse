from flask import request

from main import Parser
from zen_articles import app


@app.route('/')
def index():
    # interest = request.form.get('interest')
    parse = Parser('python')
    return f"{parse.get_articles()}"
