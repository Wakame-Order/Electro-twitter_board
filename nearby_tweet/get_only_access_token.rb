require 'net/https'
require 'base64'
require 'uri'
require 'json'

Net::HTTP.version_1_2

CONSUMER_KEY = 'cTtsePJlWipW0RE8jVMtEx03Z'
CONSUMER_SECRET = 'iLUnX4OP3AADBN7yjvjvTbMhA7raPoOXHPHGiTMsjaEKUOgf9B'
access_token = ""

bearer_token = "#{CONSUMER_KEY}:#{CONSUMER_SECRET}"
encoded_bearer_token = Base64.strict_encode64(bearer_token)
url = URI.parse("https://api.twitter.com/oauth2/token")
#search_url = URI.parse('https://api.twitter.com/1.1/search/tweets.json?q=saitama&geocode=35.866667,139.650000,10km')
search_url = URI.parse('https://api.twitter.com/1.1/search/tweets.json?q=from:sai_kyouto')

https = Net::HTTP.new(url.host, 443)
https.use_ssl = true


https.start do
  header = {}
  header["Authorization"] = "Basic #{encoded_bearer_token}"
  header["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"

  req = Net::HTTP::Post.new(url.path, header)
  req.body = "grant_type=client_credentials"

  resp = https.request(req)
  access_token = JSON.parse(resp.body)["access_token"]
  #puts resp.body
end


https.start do
  header = {}
  header["Authorization"] = "Bearer #{access_token}"
  header["Content-Type"] = "application/json"

  #puts search_url
  req = Net::HTTP::Get.new(search_url, header)
  resp = https.request(req)
  puts resp.body
end
