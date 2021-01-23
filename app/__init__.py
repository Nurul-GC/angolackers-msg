from flask import Flask
from app.config import Config
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SECRET_KEY'] = 'ANGOLACKERS_ACADEMY'
# Bootstrap(app=app)

from app import routes
