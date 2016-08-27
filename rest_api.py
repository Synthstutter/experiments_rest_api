from flask import Flask, request
import flask_sqlalchemy
import flask_restless

def run_api(database_name):
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}.db'.format(database_name)
    db = flask_sqlalchemy.SQLAlchemy(app)
    db.drop_all()
# the rest api will show up under localhost:5000/api
# the class names below are used as the request api directory.  For example: if the class is Circ(db.Model) you can request the database at localhost:5000/api/circ

    class Experiments(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        exp_name = db.Column(db.Unicode)
        box = db.Column(db.Unicode)
        datetime = db.Column(db.Unicode)
        correct = db.Column(db.Boolean)
        testing = db.Column(db.Boolean)

    db.create_all()
    manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
    manager.create_api(Experiments, methods= ['GET', 'POST'], results_per_page=None)    
    app.run(host = '0.0.0.0')
