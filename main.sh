#! /bin/sh
cd /home/pi/show_tweet
ruby ./nearby_tweet/get_only_access_token.rb >| data.json
python3 ./json2text/json2text.py
python3 ./make_picture/make_picture.py
killall sample-5
./samples/sample-5
