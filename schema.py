from __main__ import db
from flask_sqlalchemy import SQLAlchemy
import datetime



class Reading(db.Model):
    __tablename__ = "blood_pressure"
    _id = db.Column(db.Integer, primary_key=True)
    systolic = db.Column(db.String(100))
    diastolic = db.Column(db.Integer())
    date_entered = db.Column(db.Date())




    def __init__(self, reading):
        self.systolic = reading["systolic"][0]
        self.diastolic = reading["systolic"][0]
        self.date_entered = datetime.datetime.now()


    def __repr__(self):
        return f"{self.date_entered} {self.systolic} {self.date_entered}"
