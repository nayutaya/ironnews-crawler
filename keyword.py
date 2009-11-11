# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Keyword(db.Model):
  name       = db.StringProperty(required = True)
  updated_at = db.DateTimeProperty(required = True)
