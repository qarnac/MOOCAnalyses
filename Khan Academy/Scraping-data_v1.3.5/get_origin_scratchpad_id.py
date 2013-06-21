import urllib
import re
from operator import itemgetter, attrgetter
import json
import types


##################################################################################
def load_page(url):
    return urllib.urlopen(url).read()

def find_parent(url):
    htmltext = load_page(url)
    regex = '"origin_scratchpad_id": (.+?),'
    pattern = re.compile(regex)
    origin_scratchpad_id = re.findall(pattern, htmltext)
    print origin_scratchpad_id
    return origin_scratchpad_id

if __name__ == "__main__":
    find_parent("http://www.khanacademy.org/cs/mouse-cursor-and-button/1219408278")
