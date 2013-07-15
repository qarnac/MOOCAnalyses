import urllib
import re
from operator import itemgetter, attrgetter
import json
import types

total_scrape_num = 100
total_search_num = 100

def load_page(tutorial_link):
    htmltext = urllib.urlopen(tutorial_link).read()
    data = json.loads(htmltext)
    return data

def isReachMax(tutorial_link):
    data = load_page(tutorial_link)
    return data["complete"]

def count_spayoff(tutorial_link):
    data = load_page(tutorial_link)
    return len(data["scratchpads"])

def creat_tutorial_link(total_scrape_num, tutorial_id):
    tutorial_link = "https://www.khanacademy.org/api/labs/scratchpads/"+str(tutorial_id)+"/top-forks?casing=camel&limit="+str(total_search_num)
    if(isReachMax(tutorial_link)):
        if(count_spayoff(tutorial_link) == 0):
            return ""
        else:
            total_scrape_num = count_spayoff(tutorial_link)
    return "https://www.khanacademy.org/api/labs/scratchpads/"+str(tutorial_id)+"/top-forks?casing=camel&limit="+str(total_scrape_num)

def isNull(data):
    if(data):
        return data
    else:
        if (type(data) is types.IntType):
            return 0
        else:
           return "N/A"
        
def output_info(li, tutorial_id):
    print "Parent's tutorial ID: ", tutorial_id
    for i in range(len(li)):
        print li[i]
        
def get_result(tutorial_id, total_scrape_num, total_search_num):
    tutorial_link = creat_tutorial_link(total_scrape_num, tutorial_id)
    if (tutorial_link==""):
        return []
    data = load_page(tutorial_link)["scratchpads"]
    li = [[]] * len(data)
    for i in range(len(data)):
        if(type(data[i]["authorNickname"]) is unicode):
            author_nick_name = data[i]["authorNickname"].encode('utf8')
        else:
            author_nick_name = data[i]["authorNickname"]
        li[i]= (isNull(data[i]["title"]),
                isNull(author_nick_name),
                isNull(data[i]["url"]),
                isNull(data[i]["sumVotesIncremented"]),
                isNull(tutorial_id))
    li.sort(key=itemgetter(3), reverse = True)
    li[:total_scrape_num]
    #output_info(li, tutorial_id)
    #print "\n"
    return li

        
def get_first_spinoff(tutorial_id):
    #print "https://www.khanacademy.org/api/labs/scratchpads/"+str(tutorial_id)+"/top-forks?casing=camel&limit="+str(total_search_num)
    return get_result(tutorial_id, total_scrape_num, total_search_num)


if __name__ == "__main__":
    tutorial_id = 848372201
    get_first_spinoff(tutorial_id)
