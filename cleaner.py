# -*- coding: utf-8 -*-

import datetime
from google.appengine.ext import db
from article_manager import Article

print "Content-Type: text/plain"
print ""

print "cleaner"

now    = datetime.datetime.now()
expire = now - datetime.timedelta(days = 10)

print "now    : " + now.strftime("%Y-%m-%d %H:%M:%S")
print "expire : " + expire.strftime("%Y-%m-%d %H:%M:%S")

articles = db.GqlQuery("SELECT * FROM Article WHERE state = :1 AND created_at < :2 LIMIT 200",
  Article.STATE_REGISTERED, expire)

print "found  : " + str(articles.count())

db.delete(articles)

print "clean"
