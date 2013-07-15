import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
import sys
import django
import MySQLdb as mdb
from django.utils.encoding import smart_unicode
import get_parent_project_info as gppi

def update_all_spinoff_parent_project_id():
    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');
    cur = con.cursor()
    #get all urls
    cur.execute('SELECT project_id, url FROM all_spinoff WHERE parent_project_id  = ""')
    results = cur.fetchall()

    for result in results:
        project_id = result[0]
        #print id_num
        url = result[1]
        #print url
        parent_project_info = gppi.get_parent_project_info(url)
        #print parent_project_info
        cur.execute("UPDATE all_spinoff SET parent_project_id = %s, parent_project_title = %s, parent_user_id = %s where project_id = %s",(parent_project_info[0], parent_project_info[1], parent_project_info[2], project_id))

    con.close()
if __name__ == "__main__":
    update_all_spinoff_parent_project_id()
