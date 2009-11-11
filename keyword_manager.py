# -*- coding: utf-8 -*-

import datetime
from google.appengine.ext import db

class Keyword(db.Model):
  name       = db.StringProperty(required = True)
  updated_at = db.DateTimeProperty(required = True)

class KeywordManager:
  @classmethod
  def initialize(cls):
    all = db.GqlQuery("SELECT * FROM Keyword")
    if all.count(1) == 0:
      cls.put(u"鉄道")
      cls.put(u"新幹線")

  @classmethod
  def put(cls, name):
    keyword = Keyword(name = name, updated_at = datetime.datetime.now())
    keyword.put()
    return keyword

  @classmethod
  def get(cls):
    keyword = db.GqlQuery("SELECT * FROM Keyword ORDER BY updated_at ASC LIMIT 1").get()
    return keyword.name

  @classmethod
  def update(cls, name):
    keyword = db.GqlQuery("SELECT * FROM Keyword WHERE name = :1 LIMIT 1", name).get()
    if keyword is not None:
      keyword.updated_at = datetime.datetime.now()
      keyword.put()
    return keyword
