import json
import urllib.request

url='http://python-data.dr-chuck.net/comments_278085.json'
data=urllib.request.urlopen(url).read()
newdata=data.decode('utf-8')

info=json.loads(newdata)
s=0
for item in info['comments']:
      num=int(item['count'])
      s=s+num
      
print(s)
