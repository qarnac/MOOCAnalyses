import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
import get_all_tutorials_id as get_id
import get_all_tutorials_name as get_name
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
    #cur.execute("DELETE FROM org_tutorials")
    #get all records 
    cur.execute("SELECT org_tut_id FROM org_tutorials")
    results = cur.fetchall()
    
    for t_id in tutorials_id:
        #step 2: get all the name of original tutorials
        count = 0
        #print "--------------------------------------"
        #print t_id
        for org_tut_id in results:
            org_tut_id = str(org_tut_id)[1:][:-3]
            print org_tut_id
            if org_tut_id == t_id:
                count = 1
        #print count
        #print "***************************************"
        if count != 1:
            t_name = get_name.get_name(t_id)
            #step 3: insert id and name into org_tutorial table
            #database
            #insert new data
            cur.execute("INSERT INTO org_tutorials (org_tut_id, org_tut_name, inserted_time) VALUES (%s, %s, now())",(t_id, t_name))
    
    con.close()
    
if __name__ == "__main__":
    d_insert_org_tutorial()
