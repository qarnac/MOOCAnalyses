import urllib
import re
from operator import itemgetter, attrgetter
import json
import types

def load_page(tutorial_link):
    htmltext = urllib.urlopen(tutorial_link).read()
    data = json.loads(htmltext)
    return data

def get_all_spinoff_url(tutorial_id, spinoff_count):
    #print tutorial_id
    #print spinoff_count
    scratchpads_link = "https://www.khanacademy.org/api/labs/scratchpads/"+str(tutorial_id)+"/top-forks?casing=camel&limit="+str(spinoff_count)
    data = load_page(scratchpads_link)["scratchpads"]

    li = [[]] * len(data)
    i = 0
    while i < len(data):
        li[i] = data[i]["url"]
        #print li[i]
        i += 1
    return li

if __name__ == "__main__":
    tutorial_id = 827809834
    spinoff_count = 160
    get_all_spinoff_url(tutorial_id, spinoff_count)
