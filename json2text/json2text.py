#! /usr/bin/env python3
# coding:UTF-8

import json

with open("data.json", "r") as f:
    jsonData = json.load(f)
#print(json.dumps(jsonData["statuses"][0]["text"], sort_keys = True, indent = 4))
text = jsonData["statuses"][0]["text"]
print(text)

with open("tweet.txt", "w") as f2:
    f2.write(text)
