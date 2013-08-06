import MySQLdb as mdb
import sys
import os.path
import os

html_template = """\
<html>
<head>
    <title>MOOCAnalyses</title>
    <link href="/static/styles/style.css" media="screen" rel="Stylesheet" type="text/css">
</head>
<body>
    <h1>MOOCAnalyses!</h1>
    <table border=1 id = "background-image">
        <tr><th colspan=5 align = 'center'><font size='12'>User Project Distribution</th></tr>
        %(user_project_num_distribution)s
        
    </table>
</body>
</html>
"""

#%(top10_users)s
#%(top10_projects)s

def get_sql(left_range, right_range):
    if left_range == right_range:
        sql = "SELECT count(*) AS sum FROM (SELECT user_id, COUNT(*) AS sum FROM all_spinoff GROUP BY user_id) AS distribution WHERE sum = "+str(left_range)
    else:
        sql = "SELECT count(*) AS sum FROM (SELECT user_id, COUNT(*) AS sum FROM all_spinoff GROUP BY user_id) AS distribution WHERE sum >="+str(left_range)+" and sum <="+str(right_range)
    return sql

def get_distribution(left_range, right_range):
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');
    cur_1 = con.cursor()
    sql = "SELECT count(*) AS sum FROM (SELECT user_id, COUNT(*) AS sum FROM all_spinoff GROUP BY user_id) AS distribution WHERE sum =1"
    cur_1.execute(get_sql(left_range, right_range))
    user_project_num_distributions = cur_1.fetchall()
    cur_1.close()
    return user_project_num_distributions[0][0]

def application(environ, start_response):
    status = "200 OK"
    headers = [('Content-Type', 'text/html'), ]
    start_response(status, headers)
 
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');

    sql_total_number_account = "SELECT count(*) AS sum FROM user"
    sql_total_number_project = "SELECT count(*) AS sum FROM all_spinoff"
    sql_total_number_original_tutorial = "SELECT count(*) AS sum FROM org_tutorials"
    #sql_top10_users = "SELECT user_id, COUNT(*) AS sum FROM all_spinoff GROUP BY user_id ORDER BY sum DESC LIMIT 10"
    #sql_top10_projects = "SELECT project_id, project_title, spinoff_count FROM all_spinoff ORDER BY spinoff_count DESC LIMIT 10"
    
    
    cur = con.cursor()
    cur.execute(sql_total_number_account)
    total_number_account = cur.fetchall()

    cur.execute(sql_total_number_project)
    total_number_project = cur.fetchall()

    cur.execute(sql_total_number_original_tutorial)
    total_number_original_tutorial = cur.fetchall()

    #cur.execute(sql_top10_users)
    #top10_users = cur.fetchall()
    #output_top10_users = '<tr><th bgcolor = \'yellow\'>Top 10 users</th><th bgcolor = \'yellow\'>Ranking</th>'+\
                        #'<th bgcolor = \'yellow\'>User ID</th><th colspan=2 bgcolor = \'yellow\'>Total number of projects</th></tr>'
    
    #cur.execute(sql_top10_projects)
    #top10_projects = cur.fetchall()
    #output_top10_projects = '<tr><th bgcolor = \'yellow\'>Top 10 projects</th><th bgcolor = \'yellow\'>Ranking</th>'+\
                        #'<th bgcolor = \'yellow\'>Project ID</th><th bgcolor = \'yellow\'>Project Title</th>'+\
                        #'<th bgcolor = \'yellow\'>Total spinoff number</th></tr>'
    
    
    #user_ranking = 0
    #for top10_user in top10_users:
        #user_ranking += 1
        #output_top10_users += '<tr><td></td><td>'+str(user_ranking)+'</td><td>'+str(top10_user[0])+'</td><td colspan=2>'+str(top10_user[1])+'</td></tr>'

    #project_ranking = 0
    #for top10_project in top10_projects:
        #project_ranking += 1
        #output_top10_projects += '<tr><td></td><td>'+str(project_ranking)+'</td><td>'+str(top10_project[0])+'</td><td>'+str(top10_project[1])+'</td><td>'+str(top10_project[2])+'</td></tr>'


    output_user_project_num_distribution = '<tr><th bgcolor = \'yellow\'>Distribution of project number</th><th colspan=2 bgcolor = \'yellow\'>Range</th>'+\
                                           '<th colspan=2 bgcolor = \'yellow\'>Number</th></tr>'
    # 1
    project_num_1_1 = get_distribution(1, 1)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 1 </td><td colspan=2>'+str(project_num_1_1)+'</td></tr>'

    # 2
    project_num_2_2 = get_distribution(2, 2)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 2 </td><td colspan=2>'+str(project_num_2_2)+'</td></tr>'

    # 3
    project_num_3_3 = get_distribution(3, 3)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 3 </td><td colspan=2>'+str(project_num_3_3)+'</td></tr>'

    # 4
    project_num_4_4 = get_distribution(4, 4)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 4 </td><td colspan=2>'+str(project_num_4_4)+'</td></tr>'

    # 5
    project_num_5_5 = get_distribution(5, 5)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 5 </td><td colspan=2>'+str(project_num_5_5)+'</td></tr>'

    # 6
    project_num_6_6 = get_distribution(6, 6)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 6 </td><td colspan=2>'+str(project_num_6_6)+'</td></tr>'

    # 7
    project_num_7_7 = get_distribution(7, 7)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 7 </td><td colspan=2>'+str(project_num_7_7)+'</td></tr>'

    # from 8 to 10
    project_num_8_10 = get_distribution(8, 10)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 8 ~ 10 </td><td colspan=2>'+str(project_num_8_10)+'</td></tr>'

    # number from 11 to 15
    project_num_11_15 = get_distribution(11, 15)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 11 ~ 15 </td><td colspan=2>'+str(project_num_11_15)+'</td></tr>'
    
    # number from 16 to 20
    project_num_16_20 = get_distribution(16, 20)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 16 ~ 20 </td><td colspan=2>'+str(project_num_16_20)+'</td></tr>'
    
    # number from 21 to 30
    project_num_21_30 = get_distribution(21, 30)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 21 ~ 30 </td><td colspan=2>'+str(project_num_21_30)+'</td></tr>'

    # number from 31 to 50
    project_num_31_50 = get_distribution(31, 50)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 31 ~ 50 </td><td colspan=2>'+str(project_num_31_50)+'</td></tr>'
    
    # number from 51 to 100
    project_num_51_100 = get_distribution(51, 100)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 51 ~100 </td><td colspan=2>'+str(project_num_51_100)+'</td></tr>'
    
    # number from 101 to 1000
    project_num_101_1000 = get_distribution(101, 1000)
    output_user_project_num_distribution += '<tr><td></td><td colspan=2> 101 ~ 1000 </td><td colspan=2>'+str(project_num_101_1000)+'</td></tr>'
       
        
    content = html_template % {
        'total_number_account': total_number_account[0][0],
        'total_number_project': total_number_project[0][0],
        'total_number_original_tutorial': total_number_original_tutorial[0][0],
        #'top10_users': output_top10_users,
        #'top10_projects': output_top10_projects,
        'user_project_num_distribution':output_user_project_num_distribution,
    } 
    con.close()
    return [content]

