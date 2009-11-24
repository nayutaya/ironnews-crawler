# -*- coding: utf-8 -*-

import re

class BookmarkUtil:
  @classmethod
  def is_rejected_site(cls, url):
    patterns = [
      re.compile(r"http://car\.nikkei\.co\.jp/release/"), # 理由: title要素に記事タイトルを含まないため
      re.compile(r"http://markets\.nikkei\.co\.jp/"),     # 理由: title要素に記事タイトルを含まないため
      re.compile(r"http://www\.nikkei\.co\.jp/news/"),    # 理由: title要素に記事タイトルを含まないため
      re.compile(r"http://www\.pjnews\.net/"),            # 理由: title要素に記事タイトルを含まないため
    ]
    for pattern in patterns:
      if pattern.match(url):
        return True
    return False
