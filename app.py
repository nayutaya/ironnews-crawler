# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class HomePage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("hello")

if __name__ == "__main__":
  application = webapp.WSGIApplication(
    [
      (r"/", HomePage),
    ],
    debug = True)
  run_wsgi_app(application)
