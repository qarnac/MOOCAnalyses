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
import get_parent_id as gpi

def u_all_spinoff_parent_id():
    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');
    cur = con.cursor()
    #get all urls
    cur.execute("SELECT id, url FROM all_spinoff WHERE DATE(update_time)< (SELECT DATE_FORMAT( SYSDATE( ) ,  '%Y-%m-%d'))")
    results = cur.fetchall()
    #gpt.get_parent_id
    for result in results:
        id_num = result[0]
        print id_num
        url = result[1]
        #print url
        parent_id = gpi.get_parent_id(url)
        #print parent_id
        cur.execute("UPDATE all_spinoff SET parent_id = %s where id = %s",(parent_id, id_num))

    
if __name__ == "__main__":
    u_all_spinoff_parent_id()
