# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_278084.html' 
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags=soup('span')
total=0
count=0
for tag in tags:
    num=int(tag.contents[0])
    count=count+1
    total=total+num
    
print('Total is', total)
print('Count:', count)
