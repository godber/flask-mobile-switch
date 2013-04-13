#Initialization File
#Importing Flask and SQLAlchemy
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


# Create application
app = Flask(__name__)
app.config.from_object('missionops.config')
#Create SQLAlchemy object
db = SQLAlchemy(app)

from missionops import models
from missionops import views
