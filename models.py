from rest_api import db

class Circ(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    sensor= db.Column(db.Integer, nullable=False)
    datetime= db.Column(db.DateTime, nullable=False)


class Beeboxes(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    box= db.Column(db.Integer, nullable=False)
    correct= db.Column(db.Boolean, nullable=False)
    datetime= db.Column(db.DateTime, nullable=False)


    


