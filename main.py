from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

my_api = Api(app)


if os.getenv('GAE_INSTANCE'):
    db_user = os.environ.get('CLOUD_SQL_USERNAME')
    db_password = os.environ.get('CLOUD_SQL_PASSWORD')
    db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
    db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
    host = '/cloudsql/{}'.format(db_connection_name)
else:
    # Cargar configuracion local
    try:
        from configparser import ConfigParser
    except:
        # para soportar python 2.7
        from ConfigParser import ConfigParser

    dir_path = os.path.dirname(os.path.realpath(__file__))
    cp = ConfigParser()
    cp.read("{}/{}".format(dir_path, "config.ini"))

    # Configuracion para BD local
    db_user = cp.get("DEFAULT", "db_user")
    db_password = cp.get("DEFAULT", "db_password")
    db_name = cp.get("DEFAULT", "db_name")
    host = cp.get("DEFAULT", "db_host")

app.config['SQLALCHEMY_DATABASE_URI'] = "{}://{}:{}@/{}?host={}".format(
    "postgresql+psycopg2",
    db_user,
    db_password,
    db_name,
    host
)
db = SQLAlchemy(app)

from api.routes import MutantAPI
from api.routes import StatsAPI

my_api.add_resource(MutantAPI, '/mutant')
my_api.add_resource(StatsAPI, '/stats')