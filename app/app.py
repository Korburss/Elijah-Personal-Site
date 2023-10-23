from flask import Flask
import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile("config.py")

    mail.init_app(app)

    with app.app_context():
        from .home import home
        from .error import error

        app.register_blueprint(home.home_bp)
        app.register_blueprint(error.error_bp)

    if not app.debug:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='Site Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            # pylint: disable=no-member
            app.logger.addHandler(mail_handler)
        
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/site.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Site startup')

    return app