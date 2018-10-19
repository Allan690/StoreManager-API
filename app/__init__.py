from flask import Flask
from app.api.v1.views.product_views import prod
from app.api.v1.views.sale_views import sal
flaskApp = Flask(__name__)
# app.config.from_object('config.Development')

flaskApp.register_blueprint(prod)
flaskApp.register_blueprint(sal)
