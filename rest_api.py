from flask import Flask,jsonify,request
from flask.ext.sqlalchemy import SQLAlchemy

app= Flask("__none__")

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///bee_experiments.db'

db=SQLAlchemy(app)

from models import *

@app.route('/', methods=['GET'])
def home():
    posts=db.session.query(ShbBeeCircadian).all()
    return jsonify({"posts": posts[0]})

@app.route('/', methods=['POST'])
def upload_db():
    

if __name__== "__main__":
    app.run()
