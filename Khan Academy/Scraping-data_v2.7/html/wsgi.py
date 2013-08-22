#!/usr/bin/python

import sys
import django
import MySQLdb as mdb


html = """
<html>
<head>
    <title>MOOCAnalyses</title>
    <link href="/static/styles/style.css" media="screen" rel="Stylesheet" type="text/css">
</head>
<body>
    <div id="absmiddle">

    <table border=1 id = "hor-minimalist-a">
        <tr>
            <th align = 'center'><h1>MOOCAnalyses!</h1></th>
        </tr>
        <tr>
            <td align = 'center'>
                <form name="myform" method="post">
                    <select onchange="document.myform.action=this.value;">
                      <option value="description">Please choose one.....</option>
                      <option value="summary">Summary</option>
                      <option value="user_pro_distribution">User Project Distribution</option>
                      <option value="chart">Chart</option>
                    </select>
                <input type="submit" value="OK">          
            </td>
        </tr>
    </table>
</div>

</body>
</html>
"""


def application(environ, start_response):
    status = '200 OK'
    output = html
 
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
 
    return [output]
