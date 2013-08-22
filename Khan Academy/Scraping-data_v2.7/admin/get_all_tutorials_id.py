import urllib
import re

def get_ids(): 
    all_tutorials_link = "https://www.khanacademy.org/cs"
    htmltext = urllib.urlopen(all_tutorials_link).read()
    regex = ', "id": "(.+?)",'
    pattern = re.compile(regex)
    tutorial_ids = re.findall(pattern, htmltext)
    return tutorial_ids
    
if __name__ == "__main__":
    get_ids()
