# -*- coding: utf-8 -*-

import re
from datetime import timedelta
from google.appengine.ext import db
from article_manager import Article
from article_manager import ArticleManager

def get_oldest_time():
  query   = db.GqlQuery("SELECT * FROM Article ORDER BY created_at ASC LIMIT 1")
  article = query.get()
  return article.created_at

def get_newest_time():
  query   = db.GqlQuery("SELECT * FROM Article ORDER BY created_at DESC LIMIT 1")
  article = query.get()
  return article.created_at

def get_articles_by_date(date):
  begin_date = date
  end_date   = date + timedelta(days = 1)
  query      = db.GqlQuery("SELECT * FROM Article WHERE created_at >= :1 AND created_at < :2 ORDER BY created_at ASC", begin_date, end_date)
  return query

print "Content-Type: application/xml"
#print "Content-Type: text/plain"
print ""

oldest_time = get_oldest_time()
newest_time = get_newest_time()
days        = (newest_time.date() - oldest_time.date()).days + 1
dates       = [oldest_time.date() + timedelta(days = i) for i in range(days)]

print '<?xml version="1.0" encoding="UTF-8"?>'
print '<ironnews-crawler>'

print ' <oldest-time>' + oldest_time.strftime("%Y-%m-%d %H:%M:%S") + '</oldest-time>'
print ' <newest-time>' + newest_time.strftime("%Y-%m-%d %H:%M:%S") + '</newest-time>'

for date in dates:
  print ' <articles date="' + date.strftime("%Y-%m-%d") + '">'
  for article in get_articles_by_date(date):
    url = re.sub(r"&", "&amp;", article.url)
    print '  <article key="' + str(article.key().id()) + '">'
    print '   <created-at>' + article.created_at.strftime("%Y-%m-%d %H:%M:%S") + '</created-at>'
    print '   <url>' + url + '</url>'
    print '   <title>' + article.title.encode("utf-8") + '</title>'
    print '  </article>'
  print ' </articles>'

print '</ironnews-crawler>'
