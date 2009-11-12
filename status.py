# -*- coding: utf-8 -*-

import datetime
from keyword_manager import KeywordManager
from article_manager import ArticleManager

print "Content-Type: text/html; charset=utf-8"
print ""

print "<html>"
print " <head>"
print "  <title>ironnews-crawler status</title>"
print " </head>"
print " <body>"

print "  <h1>ironnews-crawler status</h1>"

print "  <h2>keywords</h2>"
print "  <table border='1'>"

for keyword in KeywordManager.all():
  print "<tr>"
  print " <td>" + (keyword.updated_at + datetime.timedelta(hours = 9)).strftime("%Y-%m-%d %H:%M") + "</td>"
  print " <td>" + keyword.name.encode("utf-8") + "</td>" # FIXME: HTML escape
  print "</tr>"

print "  </table>"

print "  <h2>latest articles</h2>"
print "  <table border='1'>"

for article in ArticleManager.latest(100):
  print "<tr>"
  print " <td>" + (article.created_at + datetime.timedelta(hours = 9)).strftime("%Y-%m-%d %H:%M") + "</td>"
  print " <td>"
  print "  <a href='" + article.url.encode("utf-8") + "'>" + article.title.encode("utf-8") + "</a>" # FIXME: HTML escape
  print " </td>"
  print "</tr>"

print "  </table>"

print " </body>"
print "</html>"
