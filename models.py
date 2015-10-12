from rest_api import db

class ShbBeeCircadian(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    box= db.Column(db.Integer, nullable=False)
    correct= db.Column(db.Boolean, nullable=False)
    datetime= db.Column(db.DateTime, nullable=False)

    def __init__(self, box,correct,datetime):
        self.box=box
        self.correct=correct
        self.datetime=datetime

    def __repr__(self):
        return '"box": {}, "correct": {}, "time": {}'.format(self.box, self.correct, self.datetime)
