# -*- coding: utf-8 -*-

import sys
sys.path.append("lib")

import datetime
from google.appengine.ext import db

import urllib
import urllib2

import simplejson

class Article(db.Model):
  url        = db.StringProperty(required = True)
  title      = db.StringProperty(required = True)
  created_at = db.DateTimeProperty(required = True, auto_now_add = True)

class Keyword(db.Model):
  name       = db.StringProperty(required = True)
  updated_at = db.DateTimeProperty(required = True)


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

class KeywordManager:
  @classmethod
  def initialize(cls):
    records = db.GqlQuery("SELECT * FROM Keyword").fetch(1000)
    db.delete(records)
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


class GoogleNews:
  @classmethod
  def create_url(cls, keyword, num):
    host = "v3.latest.ironnews-helper2.appspot.com"
    base = "http://" + host + "/google-news/search"
    params = {
      "keyword": keyword.encode("utf-8"),
      "num"    : str(num),
    }
    return base + "?" + urllib.urlencode(params)

  @classmethod
  def fetch(cls, keyword, num):
    request = urllib2.Request(
      url = cls.create_url(keyword, num))
    request.add_header("User-Agent", "ironnews")

    io = urllib2.urlopen(request)
    try:
      return io.read()
    finally:
      io.close()

  @classmethod
  def search(cls, keyword, num = 10):
    json = cls.fetch(keyword, num)
    return simplejson.loads(json)


print "Content-Type: text/plain"
print ""

#KeywordManager.initialize()

keyword = KeywordManager.get()
print keyword.encode("utf-8")

articles = GoogleNews.search(keyword, 10)
for article in articles:
  url   = article["url"]
  title = article["title"]
  print url
  print title.encode("utf-8")
  print ArticleManager.exist(url)
  ArticleManager.add(url, title)
  print ArticleManager.exist(url)

KeywordManager.update(keyword)
