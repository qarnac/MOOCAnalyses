import urllib
import re

def get_user_id(url): 
    htmltext = urllib.urlopen(url).read()
    regex = '<a href="/profile/(.+?)/'
    pattern = re.compile(regex)
    user_id = re.findall(pattern, htmltext)
    #print htmltext
    return user_id
    
if __name__ == "__main__":
    url = "https://www.khanacademy.org/cs/khan-academy/1321968556"
    get_user_id(url)
