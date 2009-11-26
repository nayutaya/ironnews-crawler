# -*- coding: utf-8 -*-

import re

CanonicalTable = (
  (re.compile(r'\A(http://[a-z]+\.yomiuri\.co\.jp/.+)\?from=[a-z0-9]+\Z'), r'\1'),
  (re.compile(r'\A(http://japan\.cnet\.com/.+)\?ref=rss\Z'), r'\1'),
  (re.compile(r'\A(http://journal\.mycom\.co\.jp/.+)\?rt=na\Z'), r'\1index.html'),
  (re.compile(r'\A(http://mainichi\.jp/.+)\?link_id=[A-Z0-9]+\Z'), r'\1'),
  (re.compile(r'\A(http://news\.searchina\.ne\.jp/.+)&pt=large\Z'), r'\1'),
  (re.compile(r'\A(http://www\.asahi\.com/.+)\?ref=rss\Z'), r'\1'),
  (re.compile(r'\A(http://www\.chunichi\.co\.jp/.+)\?ref=rank\Z'), r'\1'),
  (re.compile(r'\A(http://www\.jiji\.com/jc/c\?g=.+?)&rel=j7(&k=\d+)\Z'), r'\1\2'),
  (re.compile(r'\A(http://www\.tetsudo\.com/.+)\?tag=as\.rss\Z'), r'\1'),
)
