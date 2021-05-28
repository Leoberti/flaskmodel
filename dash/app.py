from flask import Flask
from dash.ext import site
from dash.ext import config
from dash.ext import toolbar 



def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app) 
    
    return app



 