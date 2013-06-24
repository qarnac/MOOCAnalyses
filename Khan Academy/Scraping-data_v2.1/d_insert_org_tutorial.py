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

def d_insert_org_tutorial():
    #step 1: get all the id of original tutorials
    tutorials_id = get_id.get_id()

    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb");
    cur = con.cursor()
    #delete all data in org_tutorial table
    cur.execute("DELETE FROM org_tutorials")
    
    for t_id in tutorials_id:
        #step 2: get all the name of original tutorials
        t_name = get_name.get_name(t_id)

        #step 3: insert id and name into org_tutorial table
        #database
        #insert new data
        cur.execute("INSERT INTO org_tutorials (org_tut_id, org_tut_name) VALUES (%s, %s)",(t_id, t_name))
    
    con.close()
    
if __name__ == "__main__":
    d_insert_org_tutorial()
