from flask import Flask
from dash.ext import toolbar 
from dash.ext import site


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ABACATE02"
    toolbar.init_app(app)
    site.init_app(app) 
    
    return app



 