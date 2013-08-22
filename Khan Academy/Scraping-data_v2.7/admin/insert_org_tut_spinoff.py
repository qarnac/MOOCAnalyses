import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
import get_project_info as gpi
import get_all_spinoff_url as gasu
import get_all_spinoff_url_bigger_2k as gasub2
import get_user_id as gui
import sys
import django
import MySQLdb as mdb

def is_in_db(db_project_ids, project_id):
    sign = 0
    for db_project_id in db_project_ids:
        if db_project_id[0] == project_id:
            sign = 1
    if sign == 1:
        return 1
    else:
        return 0

    
def insert_org_tut_spinoff():

    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');
    cur = con.cursor()

    cur.execute('SELECT org_tut_id, spinoff_count FROM 0810_0_original_tutorial WHERE is_checked = "0"')
    db_org_tuts = cur.fetchall()

    cur.execute('SELECT project_id FROM 0810_first_level_spinoff')
    db_project_ids = cur.fetchall()
    
    for db_org_tut in db_org_tuts:
        parent_project_id = db_org_tut[0]
        spinoff_count = db_org_tut[1]
        print parent_project_id
        if spinoff_count <= 2000 :
            org_tut_spinoff_urls = gasu.get_all_spinoff_url(parent_project_id, spinoff_count)
        else:
            org_tut_spinoff_urls = gasub2.get_all_spinoff_url_bigger_2k(parent_project_id, spinoff_count)
         
        accurate_spinoff_count = len(org_tut_spinoff_urls)
        for org_tut_spinoff_url in org_tut_spinoff_urls:
            user_id = gui.get_user_id(org_tut_spinoff_url)
            project_id = org_tut_spinoff_url[org_tut_spinoff_url.rfind("/")+1:]
            if not is_in_db(db_project_ids, project_id):
                org_tut_spinoff_info = gpi.get_project_info(project_id)
                title = org_tut_spinoff_info[0]
                created_date = org_tut_spinoff_info[4].replace("T"," ").replace("Z","")
                spinoff_count = org_tut_spinoff_info[5]
                parent_project_id = org_tut_spinoff_info[6]
                #print project_id
                cur.execute("INSERT INTO 0810_first_level_spinoff (user_id, project_id, project_title, url, created, spinoff_count, parent_project_id, org_tut_id, inserted_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, now())",
                            (user_id[0], project_id, title, org_tut_spinoff_url, created_date, spinoff_count, parent_project_id, parent_project_id))

        cur.execute('UPDATE 0810_0_original_tutorial SET is_checked = "1", checked_date = now(), a_spinoff_count = %s WHERE org_tut_id = %s', (accurate_spinoff_count, parent_project_id))
    
    con.close()
    
if __name__ == "__main__":
    insert_org_tut_spinoff()
