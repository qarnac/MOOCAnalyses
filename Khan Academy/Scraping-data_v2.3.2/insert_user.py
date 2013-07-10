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

def d_insert_user():
    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb");
    cur = con.cursor()
    #delete all data in user table
    #cur.execute("TRUNCATE TABLE user")
    cur.execute("SELECT user_id FROM first_level_spinoff WHERE user_id != 'none' GROUP BY user_id")
    results_first_level_spinoff_table = cur.fetchall()

    cur.execute("SELECT user_id FROM user")
    results_user_table = cur.fetchall()
    
    for user_id in results_first_level_spinoff_table:
        user_id = str(user_id)[2:][:-3]
        count = 0
        for user in results_user_table:
            user = str(user)[2:][:-3]
            if user == user_id:
                count = 1
        if count != 1:
            cur.execute("INSERT INTO user (user_id) VALUES (%s)",(user_id))
    
    con.close()
    
if __name__ == "__main__":
    d_insert_user()
