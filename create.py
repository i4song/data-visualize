from flask import Flask


def create_app(mode='dev'):
    app = Flask(__name__)
    
    from config import config_by_name
    app.config.from_object(config_by_name[mode])
    
    from logger import file_logger
    app.logger.addHandler(file_logger('CRITICAL'))

    from src.views import api_user
    from src.views import api_error
    app.register_blueprint(api_user)
    app.register_blueprint(api_error)
    
    return app
