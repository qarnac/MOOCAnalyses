import urllib
import re

def get_user_id(project_id): 
    all_tutorials_link = "https://www.khanacademy.org/cs/khan-academy/"+str(project_id)
    htmltext = urllib.urlopen(all_tutorials_link).read()
    regex = '<a href="/profile/(.+?)/"'
    pattern = re.compile(regex)
    user_id = re.findall(pattern, htmltext)
    #print user_id
    return user_id
    
if __name__ == "__main__":
    project_id = 1153732313
    get_user_id(project_id)
