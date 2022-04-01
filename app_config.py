
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import connexion
import os
from model import db
basedir = os.path.abspath(os.path.dirname(__file__))

application = connexion.FlaskApp(__name__)

# Read the swagger.yml file to configure the endpoints
application.add_api("swagger.yaml")
app = application.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.before_first_request
def create_tables():
    db.create_all()



