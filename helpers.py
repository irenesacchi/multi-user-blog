import os
import re
import random
import hashlib
import hmac
import time
import codecs
from string import letters

import webapp2
import jinja2

from google.appengine.ext import db


# Jinja configuration

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


# Global functions

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

## User Key

def users_key(group = 'default'):
    return db.Key.from_path('users', group)

## Blog key 

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)


## Valid Username
            
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

## Valid Passw

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

## Valid Email

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


# Authentication

secret = '7gd*&0o7I@aqr9vCPGB%$RlE4HPtNujq@^UM8Vpk3shYT05G"{VS'

## Passw Hash

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

## Salt Secure Passw

def make_salt(length = 5):
    return ''.join(random.choice(letters) for x in xrange(length))

## Check Passw Validity

def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

## Secure Cookie

def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

## Check Secure Cookie

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val
    
