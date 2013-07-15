import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
import get_all_tutorials_id as get_id
import get_spinoff
import get_user_id
import sys
import django
import MySQLdb as mdb

def d_insert_first_level_spinoff():
    #step 1: get all the id of original tutorials
    tutorials_id = get_id.get_id()

    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');
    cur = con.cursor()
    #get all original tutorials id
    #cur.execute("TRUNCATE TABLE first_level_spinoff") 
    cur.execute('SELECT org_tut_id FROM org_tutorials WHERE is_checked = "0"')
    results_org_tut_id = cur.fetchall()

    cur.execute('SELECT project_id FROM first_level_spinoff')
    results_project_id = cur.fetchall()
    
    for org_tut_id in results_org_tut_id:
        org_tut_id = str(org_tut_id[0])

        results = get_spinoff.get_first_spinoff(org_tut_id)
        for result in results:
            count = 0

            project_title = result[0]
            url = result[2]
            parent_project_id = org_tut_id
            user_id = str(get_user_id.get_user_id(url)[0])
            #user_id = str(user_id[0])
            project_id = url[url.rfind('/')+1:]
            #if not user_id:
                #user_id = ['NULL']
            
            for r_project_id in results_project_id:
                r_project_id = str(r_project_id[0])
                if r_project_id == project_id:
                    count = 1

            if count != 1:
                cur.execute("INSERT INTO first_level_spinoff (user_id, project_id, project_title, url, parent_project_id) VALUES (%s, %s, %s, %s, %s)",
                            (user_id, project_id, project_title, url, parent_project_id))
                
        cur.execute('UPDATE org_tutorials SET is_checked = "1", checked_date = current_date WHERE org_tut_id = %s', (org_tut_id))
    
    con.close()
    
if __name__ == "__main__":
    d_insert_first_level_spinoff()
