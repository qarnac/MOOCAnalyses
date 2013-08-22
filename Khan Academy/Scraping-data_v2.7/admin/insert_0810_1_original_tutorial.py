import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
import get_all_tutorials_id as gati
import get_project_info as gpi
import sys
import django
import MySQLdb as mdb

def insert_org_tutorial():
    #get all the id of original tutorials
    all_tutorial_ids = gati.get_ids()

    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb");
    cur = con.cursor()
	
    #-------------------------------------------------------------------------------
    # tags in one field
    #cur.execute("SELECT org_tut_id FROM 0810_0_original_tutorial")        
    #-------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------
    #tags in mutiple lines
    cur.execute("SELECT org_tut_id FROM 0810_1_original_tutorial")
    #-------------------------------------------------------------------------------

    db_tut_ids = cur.fetchall()
    
    for tutorial_id in all_tutorial_ids:
        count = 0
        for db_tut_id in db_tut_ids:
            if str(db_tut_id[0]) == tutorial_id:
                count = 1

        if count != 1:
            tutorial_info = gpi.get_project_info(tutorial_id)
            title = tutorial_info[0]
            category = tutorial_info[1]
            tags = tutorial_info[2]

            difficulty_dict = {'10':'Getting_Started','20':'Easy','30':'Intermediate','40':'Expert'}
            difficulty = difficulty_dict.get(str(tutorial_info[3]),'NULL')
            
            created_time = tutorial_info[4].replace("T"," ").replace("Z","")
            spinoff_count = tutorial_info[5]


            #-------------------------------------------------------------------------------
            #tags in one field
            #tmp_tag = ""
            #for tag in tags:
                #if tag == "":
                    #tmp_tag = "NULL"
                #else:
                    #tmp_tag += str(tag) + ";"
            #tag = tmp_tag
            #cur.execute("INSERT INTO 0810_0_original_tutorial (org_tut_id, org_tut_name, category, tags, difficulty, created, spinoff_count, inserted_time) VALUES (%s, %s, %s, %s, %s, %s, %s, now())",
                        #(tutorial_id, title, category, tag, difficulty , created_time, spinoff_count))
            #-------------------------------------------------------------------------------

            #-------------------------------------------------------------------------------
            #tags in mutiple lines
            if tags:
                for tag in tags:
                    cur.execute("INSERT INTO 0810_1_original_tutorial (org_tut_id, org_tut_name, category, tags, difficulty, created, spinoff_count, inserted_time) VALUES (%s, %s, %s, %s, %s, %s, %s, now())",
                                (tutorial_id, title, category, tag, difficulty , created_time, spinoff_count))
            else:
                cur.execute("INSERT INTO 0810_1_original_tutorial (org_tut_id, org_tut_name, category, tags, difficulty, created, spinoff_count, inserted_time) VALUES (%s, %s, %s, %s, %s, %s, %s, now())",
                            (tutorial_id, title, category, "NULL", difficulty , created_time, spinoff_count))

            #-------------------------------------------------------------------------------
    con.close()
    
if __name__ == "__main__":
    d_insert_org_tutorial()
