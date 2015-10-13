import rest_api

class Circ(rest_api.db.Model):
    id= rest_api.db.Column(rest_api.db.Integer, primary_key=True)
    sensor= rest_api.db.Column(rest_api.db.Integer, nullable=False)
    datetime= rest_api.db.Column(rest_api.db.DateTime, nullable=False)


class Beeboxes(rest_api.db.Model):
    id= rest_api.db.Column(rest_api.db.Integer, primary_key=True)
    box= rest_api.db.Column(rest_api.db.Integer, nullable=False)
    correct= rest_api.db.Column(rest_api.db.Boolean, nullable=False)
    datetime= rest_api.db.Column(rest_api.db.DateTime, nullable=False)


    


