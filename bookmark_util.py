# -*- coding: utf-8 -*-

import re

class BookmarkUtil:
  @classmethod
  def is_rejected_site(cls, url):
    patterns = [
      re.compile(r"http://www\.nikkei\.co\.jp/news/"),
      re.compile(r"http://markets\.nikkei\.co\.jp/kokunai/"),
    ]
    for pattern in patterns:
      if pattern.match(url):
        return True
    return False

urls = [
  "http://www.nikkei.co.jp/news/",
  "http://markets.nikkei.co.jp/kokunai/",
  "http://car.nikkei.co.jp/release/",
  "http://www.pjnews.net/",
]

for url in urls:
  print url
  print BookmarkUtil.is_rejected_site(url)
