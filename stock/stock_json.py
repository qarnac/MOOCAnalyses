import urllib
import re
import json

# get this url from google developer tools
url = "http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:AR"
"""
htmltext = urllib.urlopen(url).read()
because json takes a file not a string
Hence
"""
htmltext = urllib.urlopen(url)
data = json.load(htmltext)

print "The price is :", data["last_price"]



