# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Mueez.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

count=0

while count<7:
    url=tags[17].get('href', None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags=soup('a')
    count=count+1
    
print(url)
