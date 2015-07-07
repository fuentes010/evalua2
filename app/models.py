from flask.ext.sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/evalua2'
db = SQLAlchemy(app)

class bloom_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    seq = db.Column(db.Integer, unique=True)

class bloom_category_rev(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    seq = db.Column(db.Integer, unique=True)

class bloom_value(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    categ_id = db.Column(db.Integer, db.ForeignKey('bloom_category.id'))
    categ_rev_id = db.Column(db.Integer, db.ForeignKey('bloom_category_rev.id'))

class ra_value(db.Model):
    ID_APRENDIZAJE = db.Column(db.Integer, primary_key=True)
    NOMBRE = db.Column(db.String(200))
    ID_TIPO = db.Column(db.Integer)
    ASI = db.Column(db.Integer)
    CACA = db.Column(db.Integer)
    NUM_APREN = db.Column(db.Integer)
