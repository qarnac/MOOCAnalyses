import MySQLdb as mdb
import sys
import os.path
import os

#  <tr><td>Top 10 users</td><td colspan=3>%(top10_users)s</td></tr>
html_template = """\
<html>
<head>
    <title>MOOCAnalyses</title>
    <link href="/static/styles/style.css" media="screen" rel="Stylesheet" type="text/css">
</head>
<body>
    <h1>MOOCAnalyses!</h1>
    <table border=1 id = "background-image">
        <tr><th colspan=5 align = 'center'><font size='12'>ser Project Distribution</th></tr>
        <tr><th bgcolor = 'yellow'>Total number of accounts that we collected</th><td colspan=4>%(total_number_account)s</td></tr>
        <tr><th bgcolor = 'yellow'>Total number of projects that we collected</th><td colspan=4>%(total_number_project)s</td></tr>
        <tr><th bgcolor = 'yellow'>Total Number of original tutorials</th><td colspan=4>%(total_number_original_tutorial)s</td></tr>
        %(top10_users)s
        %(top10_projects)s
    </table>
</body>
</html>
"""

def application(environ, start_response):
    status = "200 OK"
    headers = [('Content-Type', 'text/html'), ]
    start_response(status, headers)
 
    con = mdb.connect(host="mysql1", user="xu004", passwd="TBtsTL4Xn6e4Whwh", db="khandb", charset='utf8');

    sql_total_number_account = "SELECT count(*) AS sum FROM user"
    sql_total_number_project = "SELECT count(*) AS sum FROM all_spinoff"
    sql_total_number_original_tutorial = "SELECT count(*) AS sum FROM org_tutorials"
    sql_top10_users = "SELECT user_id, COUNT(*) AS sum FROM all_spinoff GROUP BY user_id ORDER BY sum DESC LIMIT 10"
    sql_top10_projects = "SELECT project_id, project_title, spinoff_count FROM all_spinoff ORDER BY spinoff_count DESC LIMIT 10"

    cur = con.cursor()
    cur.execute(sql_total_number_account)
    total_number_account = cur.fetchall()

    cur.execute(sql_total_number_project)
    total_number_project = cur.fetchall()

    cur.execute(sql_total_number_original_tutorial)
    total_number_original_tutorial = cur.fetchall()

    cur.execute(sql_top10_users)
    top10_users = cur.fetchall()
    output_top10_users = '<tr><th bgcolor = \'yellow\'>Top 10 users</th><th bgcolor = \'yellow\'>Ranking</th>'+\
                        '<th bgcolor = \'yellow\'>User ID</th><th colspan=2 bgcolor = \'yellow\'>Total number of projects</th></tr>'
    
    cur.execute(sql_top10_projects)
    top10_projects = cur.fetchall()
    output_top10_projects = '<tr><th bgcolor = \'yellow\'>Top 10 projects</th><th bgcolor = \'yellow\'>Ranking</th>'+\
                        '<th bgcolor = \'yellow\'>Project ID</th><th bgcolor = \'yellow\'>Project Title</th>'+\
                        '<th bgcolor = \'yellow\'>Total spinoff number</th></tr>'
    
    user_ranking = 0
    for top10_user in top10_users:
        user_ranking += 1
        output_top10_users += '<tr><td></td><td>'+str(user_ranking)+'</td><td>'+str(top10_user[0])+'</td><td colspan=2>'+str(top10_user[1])+'</td></tr>'

    project_ranking = 0
    for top10_project in top10_projects:
        project_ranking += 1
        output_top10_projects += '<tr><td></td><td>'+str(project_ranking)+'</td><td>'+str(top10_project[0])+'</td><td>'+str(top10_project[1])+'</td><td>'+str(top10_project[2])+'</td></tr>'
        
    content = html_template % {
        'total_number_account': total_number_account[0][0],
        'total_number_project': total_number_project[0][0],
        'total_number_original_tutorial': total_number_original_tutorial[0][0],
        'top10_users': output_top10_users,
        'top10_projects': output_top10_projects,
    }

    

    con.close()
    return [content]
