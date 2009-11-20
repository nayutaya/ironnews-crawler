# -*- coding: utf-8 -*-

from datetime import timedelta
from google.appengine.ext import db
from article_manager import Article
from article_manager import ArticleManager

def get_oldest_date():
  query   = db.GqlQuery("SELECT * FROM Article ORDER BY created_at ASC LIMIT 1")
  article = query.get()
  return article.created_at

def get_newest_date():
  query   = db.GqlQuery("SELECT * FROM Article ORDER BY created_at DESC LIMIT 1")
  article = query.get()
  return article.created_at

#print "Content-Type: application/xml"
print "Content-Type: text/plain"
print ""

oldest_date = get_oldest_date().date()
newest_date = get_newest_date().date()
days        = (newest_date - oldest_date).days + 1
dates       = [oldest_date + timedelta(days = i) for i in range(days)]


print "<ironnews-crawler>"

print oldest_date
print newest_date
print dates

print "</ironnews-crawler>"
