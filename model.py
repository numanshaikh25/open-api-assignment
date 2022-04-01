from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class Entry(db.Model):
    """
    Entry Model
    """
    id = db.Column(db.Integer, primary_key=True)
    checked = db.Column(db.Boolean)
    name = db.Column(db.String(120))
    type = db.Column(db.String(120))
    age = db.Column(db.Integer)
    description = db.Column(db.String(120))
    date = db.Column(db.DateTime,default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Entry %r>' % self.name
    
    def __init__(self, checked, name, type, age, description,):
        
        self.checked =  checked
        self.name = name
        self.type = type
        self.age = age
        self.description =  description
        # self.date = date
        



