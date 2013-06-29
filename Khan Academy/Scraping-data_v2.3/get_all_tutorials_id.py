import urllib
import re

def get_id(): 
    all_tutorials_link = "https://www.khanacademy.org/cs/tutorials/all-tutorials"
    htmltext = urllib.urlopen(all_tutorials_link).read()
    regex = ', "id": "(.+?)", "revision"'
    pattern = re.compile(regex)
    tutorials_id = re.findall(pattern, htmltext)
    #print tutorials_id
    return tutorials_id
    
if __name__ == "__main__":
    get_id()
