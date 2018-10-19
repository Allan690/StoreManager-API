# import os
from app import flaskApp
# config_name = os.getenv('FLASK_CONFIG')
# app = create_app(config_name)

if __name__ == '__main__':
    flaskApp.run(debug=True)
