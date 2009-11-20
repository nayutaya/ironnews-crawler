# -*- coding: utf-8 -*-

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


print "<ironnews-crawler>"

print get_oldest_date()
print get_newest_date()

print "</ironnews-crawler>"
