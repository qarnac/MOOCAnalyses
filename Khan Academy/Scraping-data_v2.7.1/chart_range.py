import sys
import os.path
import os

html_template = """\
<!DOCTYPE html>
<html>
    <head>
        <link href="/static/styles/style.css" media="screen" rel="Stylesheet" type="text/css">
    </head>
    
    <body>
        <div id="absmiddle">
            <table border=0 id = "hor-minimalist-a">
                <form action="chart">
                <tr>
                    <td colspan=2>Please enter the number of ranges then press submit button:<br>
                    </td>
                </tr>
                <tr>
                    <td>First Range : </td>
                    <td><input type="text" name="value_1" value="1"> ~ <input type="text" name="value_2" value="100"><br></td>
                </tr>
                <tr>
                    <td>Second Range : </td>
                    <td><input type="text" name="value_3" value="101"> ~ <input type="text" name="value_4" value="200"><br></td>
                </tr>
                <tr>
                    <td>Third Range : </td>
                    <td><input type="text" name="value_5" value="201"> ~ <input type="text" name="value_6" value="300"><br></td>
                </tr>
                <tr>
                    <td>Fourth Range : </td>
                    <td><input type="text" name="value_7" value="301"> ~ <input type="text" name="value_8" value="400"><br></td>
                </tr>
                <tr>
                    <td>Fifth Range : </td>
                    <td><input type="text" name="value_9" value="401"> <br></td>
                </tr>
                <tr>
                    <td colspan=2><input type="submit" value="Submit">
                    </td>
                </tr>
            </form>
        </table>
    </div>
</body>
</html>
"""


def application(environ, start_response):
    status = '200 OK'
    output = html_template
 
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
 
    return [output]
