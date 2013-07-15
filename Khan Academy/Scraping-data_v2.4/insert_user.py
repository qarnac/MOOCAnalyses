import urllib
import re
from operator import itemgetter, attrgetter
import json
import types
import sys
import django
import MySQLdb as mdb

def get_user_id_from_all_spinoff(cur):
    cur.execute("SELECT parent_user_id FROM all_spinoff WHERE parent_user_id != 'NULL' GROUP BY parent_user_id")
    return cur.fetchall()

def get_user_id_from_first_level_spinoff(cur):
    cur.execute("SELECT user_id FROM first_level_spinoff WHERE user_id != 'NULL' GROUP BY user_id")
    return cur.fetchall()

def for_insert(results, results_user_table, cur):
    if results:
        for user_id in results:
            user_id = str(user_id)[2:][:-3]
            count = 0
            for user in results_user_table:
                user = str(user)[2:][:-3]
                if user == user_id:
                    count = 1
            if count != 1:
                cur.execute("INSERT INTO user (user_id) VALUES (%s)",(user_id))

def insert_user():
    #set up database
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb");
    cur = con.cursor()
    #delete all data in user table
    #cur.execute("TRUNCATE TABLE user")

    cur.execute("SELECT user_id FROM user")
    results_user_table = cur.fetchall()
    
    for_insert(get_user_id_from_first_level_spinoff(cur),results_user_table, cur)
    for_insert(get_user_id_from_all_spinoff(cur),results_user_table, cur)
    
    con.close()
    
if __name__ == "__main__":
    insert_user()
