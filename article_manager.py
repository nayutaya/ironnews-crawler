# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Article(db.Model):
  url        = db.StringProperty(required = True)
  title      = db.StringProperty(required = True)
  created_at = db.DateTimeProperty(required = True, auto_now_add = True)

class ArticleManager:
  @classmethod
  def exist(cls, url):
    articles = db.GqlQuery("SELECT * FROM Article WHERE url = :1", url)
    return (articles.count(1) > 0)

  @classmethod
  def put(cls, url, title):
    article = Article(url = url, title = title)
    article.put()
    return article

  @classmethod
  def add(cls, url, title):
    if not cls.exist(url):
      cls.put(url, title)
