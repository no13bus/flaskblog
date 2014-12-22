from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()


from app import views, models


# import os
# from flask.ext.login import LoginManager
# from flask.ext.openid import OpenID
# from config import basedir

# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(basedir, 'tmp'))