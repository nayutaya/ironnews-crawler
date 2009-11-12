# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Article(db.Model):
  CATEGORY_UNKNOWN = 0
  CATEGORY_RAIL    = 1
  CATEGORY_REST    = 2
  STATE_UNREGISTERED = 0
  STATE_REGISTERED   = 1

  created_at = db.DateTimeProperty(required = True, auto_now_add = True)
  url        = db.StringProperty(required = True)
  title      = db.StringProperty(required = True)
  category   = db.IntegerProperty(required = True, default = CATEGORY_UNKNOWN)
  state      = db.IntegerProperty(required = True, default = STATE_UNREGISTERED)

class ArticleManager:
  @classmethod
  def exist(cls, url):
    articles = db.GqlQuery("SELECT * FROM Article WHERE url = :1", url)
    return (articles.count(1) > 0)

  @classmethod
  def put(cls, url, title, category, state):
    article = Article(
      url      = url,
      title    = title,
      category = category,
      state    = state)
    article.put()
    return article

  @classmethod
  def add(cls, url, title, category = Article.CATEGORY_UNKNOWN, state = Article.STATE_UNREGISTERED):
    if not cls.exist(url):
      cls.put(url, title, category, state)

  @classmethod
  def latest(cls, limit):
    return db.GqlQuery("SELECT * FROM Article ORDER BY created_at DESC").fetch(limit)

  @classmethod
  def category_stats(cls):
    return {
      "unknown": db.GqlQuery("SELECT * FROM Article WHERE category = :1", Article.CATEGORY_UNKNOWN).count(1000),
      "rail"   : db.GqlQuery("SELECT * FROM Article WHERE category = :1", Article.CATEGORY_RAIL   ).count(1000),
      "rest"   : db.GqlQuery("SELECT * FROM Article WHERE category = :1", Article.CATEGORY_REST   ).count(1000),
    }

  @classmethod
  def state_stats(cls):
    return {
      "unregistered": db.GqlQuery("SELECT * FROM Article WHERE state = :1", Article.STATE_UNREGISTERED).count(1000),
      "registered"  : db.GqlQuery("SELECT * FROM Article WHERE state = :1", Article.STATE_REGISTERED  ).count(1000),
    }

