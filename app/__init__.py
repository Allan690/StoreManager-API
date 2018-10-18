"""Controller file that registers the blueprints of our application and creates
the flask application"""
from flask import Flask
from app.api.v1.views.product_views import prod as product_bp
from app.api.v1.views.sale_views import sal as sales_bp
from app.api.v1.views.user_view import user_dec as user_bp
# create our flask application
flask_app = Flask(__name__)
# register the blueprints of our models
flask_app.register_blueprint(product_bp)
flask_app.register_blueprint(sales_bp)
flask_app.register_blueprint(user_bp)