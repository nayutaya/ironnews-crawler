# -*- coding: utf-8 -*-

import sys
sys.path.append("lib")

from article_manager import Article
from article_manager import ArticleManager
from keyword_manager import KeywordManager
from google_news import GoogleNews

print "Content-Type: text/plain"
print ""

KeywordManager.initialize()

keyword = KeywordManager.get()
print keyword.encode("utf-8")

articles = GoogleNews.search(keyword, 30)
for article in articles:
  url   = article["url"]
  title = article["title"]
  print url
  print title.encode("utf-8")
  ArticleManager.add(url, title, Article.CATEGORY_RAIL)

KeywordManager.update(keyword)
