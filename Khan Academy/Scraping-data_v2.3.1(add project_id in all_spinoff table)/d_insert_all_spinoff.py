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
from django.utils.encoding import smart_unicode

def d_insert_all_spinoff():
    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');
    cur = con.cursor()
    #delete all data in all_spinoff table
    #cur.execute("TRUNCATE TABLE all_spinoff")
    cur.execute("SELECT user_id FROM user")
    results = cur.fetchall()
    
    for user_id in results:
        user_id = str(user_id)[3:][:-3]
        print user_id
        user_projects = get_user_project.get_user_prject(user_id)
        if user_projects:
            for user_project in user_projects:
                #print user_project[0]
                project_title = smart_unicode(user_project[0])
                url = user_project[1]
                #add project_id in all_spinoff table
                project_id = url[url.rfind('/')+1:]
                cur.execute("INSERT INTO all_spinoff (user_id, project_title, project_id, url, spinoff_count, parent_id) VALUES (%s,%s,%s,%s,%s)"
                                , (user_id, project_title, project_id, user_project[1], user_project[2], "null"))

    
if __name__ == "__main__":
    d_insert_all_spinoff()
