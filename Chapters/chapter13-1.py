# Python 3.5.1
import urllib.request
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_278081.xml '

data= urllib.request.urlopen(url).read()
    
newdata=data.decode('utf-8')


tree=ET.fromstring(newdata)
counts=tree.findall('.//count')

s=0
for count in counts:
      num=int(count.text)
      s=s+num
      
print(s)      

