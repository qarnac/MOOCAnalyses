import urllib
import re

# get this url from google developer tools
url = "https://www.google.com/finance/getprices?q=GOOG&x=NASD&i=1&p=25m&f=c&df=cpct&auto=1&ts=1366133330063&ei=GIptUbj_B560lgOu5gE"
htmltext = urllib.urlopen(url).read()
print "The price of GOOGLE is :", htmltext.split()[len(htmltext.split())-1]



