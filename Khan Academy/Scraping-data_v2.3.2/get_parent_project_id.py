import urllib
import re
from operator import itemgetter, attrgetter
import json
import types

def get_parent_id(url):
    htmltext = urllib.urlopen(url).read()
    regex = '"origin_scratchpad_id":(.+?),'
    pattern = re.compile(regex)
    parent_id = re.findall(pattern, htmltext)
    #print htmltext
    #print parent_id
    #print parent_id[0]
    if not parent_id:
        return "null"
    else:
        return parent_id[0]
    
if __name__ == "__main__":
    url = "https://www.khanacademy.org/cs/mind-of-its-own/1199478799"
    get_parent_id(url)

