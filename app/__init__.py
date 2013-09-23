#includes
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.mail import Mail
from momentjs import momentjs
from flask.ext.babel import Babel
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

#instantiate the app
app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.globals['momentjs'] = momentjs
db = SQLAlchemy(app)
babel = Babel(app)

#instantiate the login manager
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

#instantiate the mail server
mail = Mail(app)

# application specific includes
from app import views, models

if not app.debug:
	import logging
	from logging.handlers import SMTPHandler
	credentials = None
	if MAIL_USERNAME or MAIL_PASSWORD:
		credentials = (MAIL_USERNAME, MAIL_PASSWORD)
	mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@'+MAIL_SERVER, ADMINS, 'microblog failure', credentials)
	mail_handler.setLevel(logging.ERROR)
	app.logger.addHandler(mail_handler)

if not app.debug and os.environ.get('HEROKU') is None:
	import logging
	from logging.handlers import RotatingFileHandler
	file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024* 1024, 10)
	file_handler.setLevel(logging.INFO)
	file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s [in %(pathname)s:%(lineno)d]"))
	app.logger.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('microblog startup')
	
if os.environ.get('HEROKU') is not None:
	import logging
	stream_handler = logging.StreamHandler()
	app.logger.addHandler(stream_handler)
	app.logger.setLevel(logging.INFO)
	app.logger.info('microblog startup')

