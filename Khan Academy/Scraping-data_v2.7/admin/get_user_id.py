import urllib
import re

def get_user_id(url): 
    htmltext = urllib.urlopen(url).read()
    regex = '<a href="/profile/(.+?)/'
    pattern = re.compile(regex)
    user_id = re.findall(pattern, htmltext)

    if not user_id:
        return ['NOT_FOUND']
    return user_id
    
if __name__ == "__main__":
    url = "https://www.khanacademy.org/cs/level-8-random-algorithms/1354046039"
    get_user_id(url)
