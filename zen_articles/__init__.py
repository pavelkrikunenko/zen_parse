from flask import Flask

app = Flask(__name__)

import zen_articles.routes
