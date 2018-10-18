from flask import Flask
from app.api.v1.views.product_views import prod as product_bp
from app.api.v1.views.sale_views import sal as sales_bp
from app.api.v1.views.user_view import user_dec as user_bp
flaskApp = Flask(__name__)
flaskApp.config.from_object('development')

flaskApp.register_blueprint(product_bp)
flaskApp.register_blueprint(sales_bp)
flaskApp.register_blueprint(user_bp)
