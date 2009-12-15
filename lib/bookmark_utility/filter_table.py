# -*- coding: utf-8 -*-

import re

FilterTable = (
  re.compile(r'\Ahttp://car\.nikkei\.co\.jp/news/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://car\.nikkei\.co\.jp/release/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://contents\.innolife\.net/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://japan\.donga\.com/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://japanese\.donga\.com/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://mainichi\.jp/life/money/kabu/nsj/news/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://markets\.nikkei\.co\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://news\.ibc\.co\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://news\.searchina\.ne\.jp/'), # 理由: 記事の閲覧が有料であるため
  re.compile(r'\Ahttp://release\.nikkei\.co\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://rkk\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www2\.knb\.ne\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.chemicaldaily\.co\.jp/news/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.chugoku-np\.co\.jp/News/Tn'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.hab\.co\.jp/headline/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.iwate-np\.co\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.keidanren\.or\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.kentsu\.co\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.mxtv\.co\.jp/mxnews/news/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.nikkei\.co\.jp/kaigai/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.nikkei\.co\.jp/kyushu/news/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.nikkei\.co\.jp/news/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.pjnews\.net/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.tohkaishimpo\.com/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.travelvision\.jp/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.usfl\.com/Daily/News/'), # 理由: title要素に記事名が含まれていないため
  re.compile(r'\Ahttp://www\.wbs\.co\.jp/'), # 理由: title要素に記事名が含まれていないため
)
