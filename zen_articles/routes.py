from flask import request, render_template, jsonify

from main import Parser
from zen_articles import app


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        interest = request.form.get('interest')
        pars = Parser(str(interest))
        titles = []
        for item in pars.get_articles():
            titles.append(item['link'])
        return render_template("index.html", titles=titles)

    return render_template('index.html')
