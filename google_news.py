# -*- coding: utf-8 -*-

import urllib
import urllib2

import simplejson

class GoogleNews:
  @classmethod
  def create_url(cls, keyword, num):
    host = "v3.latest.ironnews-helper2.appspot.com"
    base = "http://" + host + "/google-news/search"
    params = {
      "keyword": keyword.encode("utf-8"),
      "num"    : str(num),
    }
    return base + "?" + urllib.urlencode(params)

  @classmethod
  def fetch(cls, keyword, num):
    request = urllib2.Request(
      url = cls.create_url(keyword, num))
    request.add_header("User-Agent", "ironnews")

    io = urllib2.urlopen(request)
    try:
      return io.read()
    finally:
      io.close()

  @classmethod
  def search(cls, keyword, num = 10):
    json = cls.fetch(keyword, num)
    return simplejson.loads(json)
