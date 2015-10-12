from flask import Flask,jsonify,request
import flask.ext.sqlalchemy
import flask.ext.restless

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experiments.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

class Circ(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    sensor= db.Column(db.Integer, nullable=False)
    datetime= db.Column(db.DateTime, nullable=False)


class Beeboxes(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    box= db.Column(db.Integer, nullable=False)
    correct= db.Column(db.Boolean, nullable=False)
    datetime= db.Column(db.DateTime, nullable=False)

db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Circ, methods= ['GET', 'POST', 'DELETE'])    
manager.create_api(Beeboxes, methods= ['GET', 'POST', 'DELETE'])    

app.run()
