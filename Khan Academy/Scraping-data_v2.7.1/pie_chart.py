import sys
import os.path
import os

html_template = """\
<html>
<head>
<meta charset="utf-8">
<style>

body {
  font: 10px sans-serif;
}

.arc path {
  stroke: #fff;
}

</style>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script type="text/javascript">
var request =
{
QueryString : function(val)
{
var uri = window.location.search;
var url = window.location.href;
var re = new RegExp("" +val+ "=([^&?]*)", "ig");
return ((uri.match(re))?(uri.match(re)[0].substr(val.length+1)):null);
}
}
</script>
</head>
<body>
<h1 align = 'center'>Chart for projects distribution</h1>

<script type="text/javascript">
document.write("Chart Ranges:<br/>");
for (var i=1; i<10; i++)
{
    var input = "value_" + i
    var rt = request.QueryString(input);
    document.write(rt);
    if (i % 2 == 0)
    {
        document.write("<br/>");
    }
    else
    {
        document.write(" ~ ");
    }
}
document.write("<br/>");
</script>




<script>

var width = 1200,
    height = 700,
    radius = Math.min(width, height) / 2;

var color = d3.scale.ordinal()
    .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c"]);

var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    .innerRadius(0);

var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.Number; });

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

d3.csv("/static/user_pro_distribution_data.csv", function(error, data) {

  data.forEach(function(d) {
    d.Number = +d.Number;
  });

  var g = svg.selectAll(".arc")
      .data(pie(data))
    .enter().append("g")
      .attr("class", "arc");

  g.append("path")
      .attr("d", arc)
      .style("fill", function(d) { return color(d.data.Range); });

  g.append("text")
      .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
      .attr("dy", ".35em")
      .style("text-anchor", "middle")
      .text(function(d) { return d.data.Range + d.data.Number;});

});

</script>
</body></html>
"""


def application(environ, start_response):
    status = '200 OK'
    output = html_template
 
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
 
    return [output]
