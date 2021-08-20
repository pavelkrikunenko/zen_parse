from zen import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interest = db.Column(db.String(250))
    title = db.Column(db.String(250), index=True, unique=True)
    text = db.Column(db.Text)

    def __repr__(self):
        return self.title
