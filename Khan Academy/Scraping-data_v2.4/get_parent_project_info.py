import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
import get_user_id

def get_parent_project_info(url):
    htmltext = urllib.urlopen(url).read()
    regex = '"origin_scratchpad": {[\s\S]*, "id": (.+?), "translated_title": "(.+?)", "slug": '
    pattern = re.compile(regex)
    parent_project_info = re.findall(regex, htmltext)

    if not parent_project_info:
        return ["NULL", "NULL", "NULL"]
    else:
        parent_project_id = parent_project_info[0][0]
        parent_project_title = parent_project_info[0][1]
        parent_url = "https://www.khanacademy.org/cs/khan-academy/" + parent_project_id
        parent_user_id = str(get_user_id.get_user_id(parent_url)[0])
        #print parent_url
        #print [parent_project_id,parent_project_title,parent_user_id]
        return [parent_project_id,parent_project_title,parent_user_id]
    
if __name__ == "__main__":
    url = "https://www.khanacademy.org/cs/keycode/991483645"
    get_parent_project_info(url)

