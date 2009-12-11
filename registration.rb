#! ruby -Ku

require "cgi"
require "open-uri"
require "rubygems"
require "json"
gem "nayutaya-bookmark-utility"
require "bookmark_utility"
gem "nayutaya-wsse"
require "wsse"

username, password = File.open("registration.id") { |file| [file.gets.chomp, file.gets.chomp] }

#host = "localhost:8080"
host = "ironnews-crawler1.appspot.com"

10.times {
  get_url = "http://#{host}/api/get-unregistered-articles"
  json    = open(get_url) { |io| io.read }

  articles = JSON.parse(json)
  articles.sort_by { rand }.each { |article|
    p article
    url = article["url"]
    canonical_url = BookmarkUtility.get_canonical_url(url)
    add_url = "http://ironnews.nayutaya.jp/api/add_article?url1=" + CGI.escape(canonical_url)
    wsse    = Wsse::UsernameToken.build(username, password).format
    json    = open(add_url, {"X-WSSE" => wsse}) { |io| io.read }
    ret     = JSON.parse(json)
    article_id = ret["result"]["1"]["article_id"]

    tag_url = "http://ironnews.nayutaya.jp/api/add_tags?article_id=#{article_id}&tag1=" + CGI.escape("googleニュース")
    wsse    = Wsse::UsernameToken.build(username, password).format
    open(tag_url, {"X-WSSE" => wsse}) { |io| io.read }

    set_url = "http://#{host}/api/set-registered-article?url=" + CGI.escape(url)
    open(set_url) { |io| io.read }

    sleep(0.5)
  }
}
