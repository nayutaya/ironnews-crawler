# -*- coding: utf-8 -*-

import sys
sys.path.append("lib")

import datetime
import time
import base64
import sha
import random
import urllib
import urllib2
import re
from google.appengine.ext import db
from article_manager import Article

import simplejson
from bookmark_utility import BookmarkUtility

def read_credential():
  f = open("config/ironnews.id")
  try:
    username = f.readline().strip()
    password = f.readline().strip()
    return dict(username = username, password = password)
  finally:
    f.close()

def create_wsse_token(username, password):
  created = re.sub(u"\.\d+$", "", datetime.datetime.now().isoformat()) + "Z"
  nonce   = sha.sha(str(time.time() + random.random())).digest()
  digest  = sha.sha(nonce + created + password).digest()

  nonce64  = base64.b64encode(nonce)
  digest64 = base64.b64encode(digest)

  format = 'UsernameToken Username="%(u)s", PasswordDigest="%(p)s", Nonce="%(n)s", Created="%(c)s"'
  value  = dict(u = username, p = digest64, n = nonce64, c = created)
  return format % value

def set_registered(url):
  article = db.GqlQuery("SELECT * FROM Article WHERE url = :1 LIMIT 1", url).get()
  if article:
    article.state = Article.STATE_REGISTERED
    article.put()

def get_articles():
  return db.GqlQuery("SELECT * FROM Article WHERE state = :1 ORDER BY created_at ASC", Article.STATE_UNREGISTERED).fetch(50)

def add_article(credential, url):
  wsse_token = create_wsse_token(credential["username"], credential["password"])

  request = urllib2.Request(
    url = "http://ironnews.nayutaya.jp/api/add_article?" + urllib.urlencode({"url1": url}))
  request.add_header("X-WSSE", wsse_token)

  io = urllib2.urlopen(request)
  try:
    return simplejson.loads(io.read())
  finally:
    io.close()

def add_tag(credential, article_id, tag):
  wsse_token = create_wsse_token(credential["username"], credential["password"])

  request = urllib2.Request(
    url = "http://ironnews.nayutaya.jp/api/add_tags?" + urllib.urlencode({"article_id": article_id, "tag1": tag.encode("utf-8")}))
  request.add_header("X-WSSE", wsse_token)

  io = urllib2.urlopen(request)
  try:
    return simplejson.loads(io.read())
  finally:
    io.close()


print "Content-Type: text/plain"
print ""

print "feeder"

credential = read_credential()

articles = get_articles()
urls     = [article.url for article in articles]
random.shuffle(urls)

for original_url in urls[0:3]:
  print "---"
  print original_url

  canonical_url = BookmarkUtility.get_canonical_url(original_url)
  print canonical_url

  result1 = add_article(credential, canonical_url)
  print result1

  article_id = result1["result"]["1"]["article_id"]

  result2 = add_tag(credential, article_id, u"googleニュース")
  print result2

  set_registered(original_url)
