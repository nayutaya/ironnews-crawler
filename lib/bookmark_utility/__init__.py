# -*- coding: utf-8 -*-

import re

from canonical_table import CanonicalTable
from filter_table import FilterTable

class BookmarkUtility:
  @classmethod
  def get_canonical_url(cls, url):
    url1 = url2 = url
    for (pattern, replace) in CanonicalTable:
      url2 = re.sub(pattern, replace, url1)
      if url2 != url1: break
      url1 = url2

    return url2

  @classmethod
  def reject(cls, url):
    for pattern in FilterTable:
      if pattern.search(url) is not None:
        return True
    return False
