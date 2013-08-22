import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
  
def get_project_info(project_id):
    url = "https://www.khanacademy.org/api/labs/scratchpads/"+str(project_id)
    htmltext = urllib.urlopen(url)
    data = json.load(htmltext)

    return [data["title"], data["category"], data["tags"], data["difficulty"], data["date"], data["spinoff_count"], data["origin_scratchpad_id"]]
    
if __name__ == "__main__":
    project_id = 1224019212
    get_project_info(project_id)

