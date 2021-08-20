from flask import request, render_template

from zen.zen_parser import Parser
from zen import app
from zen.models import Article


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        interest = request.form.get('interest')
        pars = Parser(str(interest))
        pars.get_articles()
        titles = Article.query.all()
        return render_template("index.html", titles=titles, url=pars.url)
    titles = Article.query.all()
    return render_template('index.html', titles=titles)


@app.route('/articles/<int:id>', methods=['post'])
def article(id):
    article = Article.query.filter_by(id=id).first()
    return render_template('article.html', article=article)
