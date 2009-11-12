# -*- coding: utf-8 -*-

import datetime
from keyword_manager import KeywordManager

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
  print " <td>" + keyword.name.encode("utf-8") + "</td>" # FIXME: HTML escape
  print " <td>" + (keyword.updated_at + datetime.timedelta(hours = 9)).strftime("%Y-%m-%d %H:%M") + "</td>"
  print "</tr>"

print "  </table>"

print "  <h2>latest articles</h2>"

print " </body>"
print "</html>"
