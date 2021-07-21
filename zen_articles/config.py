import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                             'sqlite:///' + os.path.join(basedir, 'zen.db')
    SQLALCEMY_TRACK_MODIFICATIONS = False
