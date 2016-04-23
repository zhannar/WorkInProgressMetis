# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
#import re

from BeautifulSoup import *

url = "http://www.digital.nyc/startups"

#http://www.digital.nyc/startups
#http://www.digital.nyc/startups?page=1
#http://www.digital.nyc/startups?page=373


html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

scripts = soup.findAll('script')

print columns

'''

#, text=pattern, attrs={'class' : 'pos'})

# Find the list of links to fully go through startups through

# Retrieve all of the anchor spans
links_collection = soup('a')


count = 0

for extracted_link in links_collection:
    if count > 10:
        break

    dir(extracted_link)

    #print type(extracted_link)
    #print extracted_link
    if "/startups/" in extracted_link.:
        #print True
        #print extracted_link
    count += 1

#print type(links_collection)
#print links_collection



sum = 0
for span in spans_collection:
   sum += int(span.contents[0])
   # Look at the parts of a tag

print sum
'''