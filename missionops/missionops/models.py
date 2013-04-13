#Imort app and db objects from msldata
from missionops import db
from missionops import app
#Import Admin, SqlaMOdel and Filters
from flask.ext.admin.contrib import sqlamodel
import flask
import flask.ext.restless
import flask.ext.sqlalchemy

class Switch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    switch_state = db.Column(db.Boolean, default=False)
    
    def __init__(self, switch_state):
        self.switch_state = switch_state

class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32), unique=True)
    value = db.Column(db.String)
    
    def __init__(self, title, value):
        self.key = title
        self.value = value


db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Switch, methods=['GET', 'POST', 'DELETE','PUT'])
manager.create_api(Config, methods=['GET', 'POST', 'DELETE'])