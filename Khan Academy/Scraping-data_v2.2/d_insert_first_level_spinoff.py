import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
import get_all_tutorials_id as get_id
import get_all_tutorials_name as get_name
import get_spinoff
import get_user_id
import get_user_project
import sys
import django
import MySQLdb as mdb

def d_insert_first_level_spinoff():
    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');
    cur = con.cursor()
    #get all original tutorials id
    cur.execute("TRUNCATE TABLE first_level_spinoff") 
    cur.execute("SELECT org_tut_id FROM org_tutorials")
    results = cur.fetchall()
    
    for org_tut_id in results:
        org_tut_id = str(org_tut_id)[1:][:-3]
        results = get_spinoff.get_first_spinoff(org_tut_id)
        for result in results:
            #database fields
            #1:call get_user_id to get user id
            #2:rfind('\') from url then cut it
            #3:result[0]: project_title
            #4:result[2]: url
            #5:result[3]: parent's id

            project_title = result[0]
            url = result[2]
            parent_id = org_tut_id
            user_id = get_user_id.get_user_id(url)
            project_id = url[url.rfind('/')+1:]
            if not user_id:
                user_id = "['none']"
            user_id = str(user_id)[2:][:-2]
            #print user_id
            #print project_id
            #print project_title
            #print url
            #print parent_id
            cur.execute("INSERT INTO first_level_spinoff (user_id, project_id, project_title, url, parent_id) VALUES (%s, %s, %s, %s, %s)",
                        (user_id, project_id, project_title, url, parent_id))
    
    con.close()
    
if __name__ == "__main__":
    d_insert_first_level_spinoff()
