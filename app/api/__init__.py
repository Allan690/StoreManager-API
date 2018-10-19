from flask import Flask
app = Flask(__name__)
app.config.from_object('config.Testing')

import app.api.views

app.register_blueprint(app.api.views, url_prefix='/api/v1/')
