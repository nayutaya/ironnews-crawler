# -*- coding: utf-8 -*-

import sys
sys.path.append("lib")

import simplejson
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from article_manager import Article
from article_manager import ArticleManager

class GetUnregisteredArticles(webapp.RequestHandler):
  def get(self):
    callback = self.request.get("callback")

    articles = ArticleManager.unregistered(10)

    result = []
    for article in articles:
      result.append({
        "url"  : article.url,
        "title": article.title,
      })

    json = simplejson.dumps(result, separators=(',',':'))
    if callback != "": json = callback + "(" + json + ")"
    self.response.headers["Content-Type"] = "text/javascript"
    self.response.out.write(json)

class HomePage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("hello")

if __name__ == "__main__":
  application = webapp.WSGIApplication(
    [
      (r"/api/get-unregistered-articles", GetUnregisteredArticles),
      (r"/", HomePage),
    ],
    debug = True)
  run_wsgi_app(application)
