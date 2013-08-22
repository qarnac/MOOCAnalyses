import urllib
import re
from operator import itemgetter, attrgetter
import json
import types

def load_page(tutorial_link):
    htmltext = urllib.urlopen(tutorial_link).read()
    data = json.loads(htmltext)
    return data

def get_scratchpads_link(tutorial_id, loop_times, cur_times, cursor):
    if cur_times == 0:
        scratchpads_link = "https://www.khanacademy.org/api/labs/scratchpads/"+str(tutorial_id)+"/top-forks?casing=camel&limit=1000"
    else:
        scratchpads_link = "https://www.khanacademy.org/api/labs/scratchpads/"+str(tutorial_id)+"/top-forks?casing=camel&limit=1000&page=0&cursor=" + str(cursor)
    return scratchpads_link

def get_all_spinoff_url_bigger_2k(tutorial_id, spinoff_count):
    #print tutorial_id
    #print spinoff_count
    if spinoff_count % 1000 != 0:
        loop_times = spinoff_count / 1000 + 1
    else:
        loop_times = spinoff_count / 1000
    #print loop_times
    cur_times = 0
    cursor = ""
    scratchpads_link = get_scratchpads_link(tutorial_id, loop_times, cur_times, cursor)
    #print scratchpads_link

    li = []
    while cur_times < loop_times :
        data = load_page(scratchpads_link)["scratchpads"]
        if not load_page(scratchpads_link)["complete"]:
            cursor = load_page(scratchpads_link)["cursor"]
        else:
            cur_times = loop_times
        #print cursor
        i = 0
        while i < len(data):
            li.append(data[i]["url"])
            #print li[j][i]
            i += 1
            
        cur_times += 1
        scratchpads_link = get_scratchpads_link(tutorial_id, loop_times, cur_times, cursor)
        #print scratchpads_link
    #print li
    return li

if __name__ == "__main__":
    tutorial_id = 825241936
    spinoff_count = 3605
    get_all_spinoff_url_bigger_2k(tutorial_id, spinoff_count)
