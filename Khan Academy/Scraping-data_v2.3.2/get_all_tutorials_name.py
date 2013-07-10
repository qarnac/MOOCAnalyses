import urllib
import re
import json


def get_name(tutorial_id): 
    link = "https://www.khanacademy.org/api/v1/autocompleteindex"
    htmltext = urllib.urlopen(link).read()
    data = json.loads(htmltext)["scratchpads"]
    #print data[tutorial_id]
    return data[tutorial_id]
    
if __name__ == "__main__":
    get_name("827809834")
