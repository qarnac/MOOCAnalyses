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

def main():
    #step 1: get all the id of original tutorials
    tutorials_id = get_id.get_id()
    
    for t_id in tutorials_id:
        #step 2: get all the name of original tutorials
        t_name = get_name.get_name(t_id)
        
        #step 3: insert id and name into org_tutorial table
        #database
        
        #step 4: From the result of step 3, call get_name to first level totorial info
        get_spinoff.get_first_spinoff(t_id)
        
        #step 5: Insert into first_level_spinoff table
        #database
        
        #step 6: From the result of step 5, call get_user_id to get user id
        user_id = get_user_id.get_user_id(t_id)

        #step 7: insert user info into user table
        #database

        #step 8: Call get_user_project to get all related project
        get_user_project.get_user_project(user_id)
        
        #step 9: go back to step 4 for three times (second & third level)
    
if __name__ == "__main__":
    main()
