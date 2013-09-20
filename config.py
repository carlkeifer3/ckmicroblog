import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-wil-never-guess'

OPENID_PROVIDERS = [
	{ 'name':'Google', 'url':'https://www.google.com/accounts/o8/id'},
	{ 'name':'Yahoo', 'url':'https://me.yahoo.com'},	
	{ 'name':'AOL', 'url':'https://openid.aol.com/<username>'},
	{ 'name':'Flickr', 'url':'https://www.flickr.com/<username>'},
	{ 'name':'MyOpenID', 'url':'https://www.myopenid.com'}]
	
# mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'carlkeifer3@gmail.com'
MAIL_PASSWORD = None

#administrator list
ADMINS = ['carlkeifer3@gmail.com']

#pagination
POSTS_PER_PAGE = 3

#Search options
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# -*- coding: utf-8 -*-

# ...
# available languages
LANGUAGES = {
	'en': 'English',
	'es': 'Espanol'	
}

