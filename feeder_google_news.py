# -*- coding: utf-8 -*-

import datetime
import time
import base64
import sha
import random
from google.appengine.ext import db
from article_manager import Article

def read_credential():
  f = open("config/ironnews.id")
  try:
    username = f.readline().strip()
    password = f.readline().strip()
    return dict(username = username, password = password)
  finally:
    f.close()

def create_wsse_token(username, password):
  created = datetime.datetime.now().isoformat() + "Z"
  nonce   = base64.b64encode(sha.sha(str(time.time() + random.random())).digest())
  digest  = base64.b64encode(sha.sha(nonce + created + password).digest())

  format = 'UsernameToken Username="%(u)s", PasswordDigest="%(p)s", Nonce="%(n)s", Created="%(c)s"'
  value  = dict(u = username, p = digest, n = nonce, c = created)
  return format % value


print "Content-Type: text/plain"
print ""

print "feeder"

credential = read_credential()
wsse_token = create_wsse_token(credential["username"], credential["password"])
print credential
print wsse_token

# TODO: WSSE認証
# TODO: 未登録記事の取得
# TODO: 未登録記事を登録記事に状態変更
# TODO: 記事の登録
# TODO: 記事にタグを打つ
