from zen_articles import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'))
    title = db.Column(db.String(250), index=True, unique=True)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interest = db.Column(db.String(250), unique=True, nullable=False)
    articles = db.relationship('Article', backref='interest', lazy='dynamic')

    def __repr__(self):
        return self.interest
