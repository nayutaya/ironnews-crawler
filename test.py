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

print "Content-Type: text/plain"
print ""

#print "test"

#article = Article(url = "hoge", title = "huga")
#article.put()

def create_url(keyword, num):
  host = "v3.latest.ironnews-helper2.appspot.com"
  params = {
    "keyword": keyword.encode("utf-8"),
    "num"    : str(num),
  }
  url = "http://" + host + "/google-news/search?" + urllib.urlencode(params)
  return url

def search_articles_by_google_news(keyword, num):
  url = create_url(keyword, num)
  request = urllib2.Request(url = url)
  request.add_header("User-Agent", "ironnews")

  io = urllib2.urlopen(request)
  try:
    json = io.read()
  finally:
    io.close()

  obj = simplejson.loads(json)
  return obj

def exist_article(url):
  articles = db.GqlQuery("SELECT * FROM Article WHERE url = :1", url)
  return (articles.count(1) > 0)

def add_article(url, title):
  article = Article(url = url, title = title)
  article.put()
  return article

articles = search_articles_by_google_news(u"鉄道", 10)
for article in articles:
  url   = article["url"]
  title = article["title"]
  print url
  print title.encode("utf-8")
  print exist_article(url)
  if not exist_article(url):
    add_article(url, title)
  print exist_article(url)
