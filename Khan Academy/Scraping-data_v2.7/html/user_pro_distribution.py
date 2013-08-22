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

def generate_range_row_code(begin, end):
    project_num = get_distribution(begin, end)
    return'<tr><td></td><td colspan=2> ' + str(begin) + ' ~ ' + str(end) + '</td><td colspan=2>'+str(project_num)+'</td></tr>'

def application(environ, start_response):
    status = "200 OK"
    headers = [('Content-Type', 'text/html'), ]
    start_response(status, headers)
 
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');

    sql_total_number_account = "SELECT count(*) AS sum FROM user"
    sql_total_number_project = "SELECT count(*) AS sum FROM all_spinoff"
    sql_total_number_original_tutorial = "SELECT count(*) AS sum FROM org_tutorials"  
    
    cur = con.cursor()
    cur.execute(sql_total_number_account)
    total_number_account = cur.fetchall()

    cur.execute(sql_total_number_project)
    total_number_project = cur.fetchall()

    cur.execute(sql_total_number_original_tutorial)
    total_number_original_tutorial = cur.fetchall()

    output_user_project_num_distribution = '<tr><th bgcolor = \'yellow\'>Distribution of project number</th><th colspan=2 bgcolor = \'yellow\'>Range</th>'+\
                                           '<th colspan=2 bgcolor = \'yellow\'>Number</th></tr>'
    range_list = [10,20,30,40,50,1000]
    range_count = len(range_list)
    count = 0
    while count < len(range_list):
        if count == 0:
            begin = 1
        else:
            begin = range_list[count - 1]
        end = range_list[count]
        output_user_project_num_distribution += generate_range_row_code(begin, end)
        count += 1
    
    content = html_template % {
        'total_number_account': total_number_account[0][0],
        'total_number_project': total_number_project[0][0],
        'total_number_original_tutorial': total_number_original_tutorial[0][0],
        'user_project_num_distribution':output_user_project_num_distribution,
    } 
    con.close()
    return [content]

