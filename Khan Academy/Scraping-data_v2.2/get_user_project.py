import urllib
import re
from operator import itemgetter, attrgetter
import json
import types

def creat_user_projects_scratch_link(user_id):
    return "https://www.khanacademy.org/api/labs/user/scratchpads?username="+user_id

def load_page(tutorial_link):
    htmltext = urllib.urlopen(tutorial_link).read()
    try:
        data = json.loads(htmltext)
    except ValueError:
        return 0
    return data

def isNull(data):
    if(data):
        return data
    else:
        if (type(data) is types.IntType):
            return 0
        else:
           return "N/A" 

def get_all_data(user_id):
    if (load_page(creat_user_projects_scratch_link(user_id))):
        data = load_page(creat_user_projects_scratch_link(user_id))["scratchpads"]
        li = [[]] * len(data)
        for i in range(len(data)):
            li[i]= ((isNull(data[i]["title"])),isNull(data[i]["url"]),isNull(data[i]["spinoff_count"]))
        li.sort(key=itemgetter(1))
        return li
    return 0
	
def get_user_prject(user_id):
    #print get_all_data(user_id)
    return get_all_data(user_id)
    
if __name__ == "__main__":
    user_id = "ldemoss"
    get_user_prject(user_id)
