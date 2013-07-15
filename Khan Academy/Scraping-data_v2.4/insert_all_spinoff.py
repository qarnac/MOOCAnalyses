import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
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
    cur.execute('SELECT user_id FROM user WHERE is_checked = "0"')
    results_user_id = cur.fetchall()

    cur.execute('SELECT project_id FROM all_spinoff')
    results_project_id = cur.fetchall()
    
    
    for user_id in results_user_id:
        user_id = str(user_id[0])
        print user_id
        user_projects = get_user_project.get_user_prject(user_id)
        if user_projects:
            for user_project in user_projects:
                #print user_project[0]
                project_title = smart_unicode(user_project[0])
                url = user_project[1]
                project_id = url[url.rfind('/')+1:]

                count = 0
                for r_project_id in results_project_id:
		    r_project_id = str(r_project_id[0])
		    #print r_project_id
                    if r_project_id == project_id:
                        count = 1
                if count != 1:
                    cur.execute("INSERT INTO all_spinoff (user_id, project_title, project_id, url, spinoff_count, parent_project_id, parent_project_title, parent_user_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                                    , (user_id, project_title, project_id, user_project[1], user_project[2], "", "", ""))

        cur.execute('UPDATE user SET is_checked = "1", checked_date = current_date WHERE user_id = %s', (user_id))

    
if __name__ == "__main__":
    d_insert_all_spinoff()
