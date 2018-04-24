import urllib2
from HTMLParser import HTMLParser
import sys

# Grab image url
response = urllib2.urlopen('https://apod.nasa.gov/apod/ap180423.html')
html = response.read()

class ImageHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   if value[len(value)-3:len(value)]=="jpg":
                       #print value
                       self.output=value
'''
<img src="image/1804/IC4592_WiseAntonucciR_960.jpg" alt="See Explanation.  Clicking on the picture will download
 the highest resolution version available." style="max-width:100%">
'''

parser = ImageHTMLParser()
parser.feed(html)
imgurl='https://apod.nasa.gov/apod/'+ parser.output
print imgurl
#https://apod.nasa.gov/apod/image/1804/IC4592_WiseAntonucciR_960.jpg

# Save the file
img = urllib2.urlopen(imgurl)
localFile = open('result.jpg', 'wb')
localFile.write(img.read())
localFile.close()

