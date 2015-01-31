#!/usr/bin/python
import csv
import sys

xml_header="""<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/xsl" href="#stylesheet"?>
<!DOCTYPE doc [
<!ATTLIST xsl:stylesheet
id ID #REQUIRED>
]>
<doc>
 <!--Start XSL-->
 <xsl:stylesheet id="stylesheet"
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >

  <xsl:template match="xsl:stylesheet" />
  <xsl:template match="/doc">
   <html>
  <head>
   <style>
	 .TaskTable {
	   margin:0px 0px 10px 0px;padding:0px;
	   width:260px;
	   height:140px;
	   border:2px solid #007fff;
	   page-break-inside: avoid !important;

	   -moz-border-radius-bottomleft:0px;
	   -webkit-border-bottom-left-radius:0px;
	   border-bottom-left-radius:0px;

	   -moz-border-radius-bottomright:0px;
	   -webkit-border-bottom-right-radius:0px;
	   border-bottom-right-radius:0px;

	   -moz-border-radius-topright:0px;
	   -webkit-border-top-right-radius:0px;
	   border-top-right-radius:0px;

	   -moz-border-radius-topleft:0px;
	   -webkit-border-top-left-radius:0px;
	   border-top-left-radius:0px;
	 }.TaskTable table{
		 border-collapse: collapse;
			 border-spacing: 0;
	   width:100%;
	   height:100%;
	   margin:0px;padding:0px;
	 }.TaskTable tr:last-child td:last-child {
	   -moz-border-radius-bottomright:0px;
	   -webkit-border-bottom-right-radius:0px;
	   border-bottom-right-radius:0px;
	 }
	 .TaskTable table tr:first-child td:first-child {
	   -moz-border-radius-topleft:0px;
	   -webkit-border-top-left-radius:0px;
	   border-top-left-radius:0px;
	 }
	 .TaskTable table tr:first-child td:last-child {
	   -moz-border-radius-topright:0px;
	   -webkit-border-top-right-radius:0px;
	   border-top-right-radius:0px;
	 }.TaskTable tr:last-child td:first-child{
	   -moz-border-radius-bottomleft:0px;
	   -webkit-border-bottom-left-radius:0px;
	   border-bottom-left-radius:0px;
	 }.TaskTable tr:hover td{
	   background-color:#ffffff;


	 }
	 .TaskTable td{
	   vertical-align:middle;
	   background-color:#ffffff;
	   border:0px solid #007fff;
	   border-width:0px 0px 0px 0px;
	   text-align:left;
	   padding:7px;
	   font-size:10px;
	   font-family:Arial;
	   font-weight:normal;
	   color:#000000;
	 }.TaskTable tr:last-child td{
	   border-width:0px 0px 0px 0px;
	 }.TaskTable tr td:last-child{
	   border-width:0px 0px 0px 0px;
	 }.TaskTable tr:last-child td:last-child{
	   border-width:0px 0px 0px 0px;
	 }
	 .TaskTable tr:first-child td{
		 background:-o-linear-gradient(bottom, #007fff 5%, #007fff 100%);	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #007fff), color-stop(1, #007fff) );
	   background:-moz-linear-gradient( center top, #007fff 5%, #007fff 100% );
	   filter:progid:DXImageTransform.Microsoft.gradient(startColorstr="#007fff", endColorstr="#007fff");	background: -o-linear-gradient(top,#007fff,007fff);

	   background-color:#007fff;
	   border:0px solid #007fff;
	   text-align:center;
	   border-width:0px 0px 0px 0px;
	   font-size:14px;
	   font-family:Arial;
	   font-weight:bold;
	   color:#ffffff;
	 }
	 .TaskTable tr:first-child:hover td{
	   background:-o-linear-gradient(bottom, #007fff 5%, #007fff 100%);	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #007fff), color-stop(1, #007fff) );
	   background:-moz-linear-gradient( center top, #007fff 5%, #007fff 100% );
	   filter:progid:DXImageTransform.Microsoft.gradient(startColorstr="#007fff", endColorstr="#007fff");	background: -o-linear-gradient(top,#007fff,007fff);

	   background-color:#007fff;
	 }
	 .TaskTable tr:first-child td:first-child{
	   border-width:0px 0px 0px 0px;
	 }
	 .TaskTable tr:first-child td:last-child{
	   border-width:0px 0px 0px 0px;
	 }

	 .TaskTable td.id {
	   padding: 5px 5px 5px 5px;
	   font-weight:normal;
	   font-size:10px;
	   height: 12px;
	 }

	 .TaskTable td.name {
	   padding: 5px 5px 5px 5px;
	   font-weight:bold;
	   font-size:12px;
	   height: 12px;
	 }

	 .TaskTable td.empty {
	 }

	 .TaskTable td.projects {
	   padding: 0px 5px 0px 5px;
	   font-weight:normal;
	   font-size:10px;
	   height: 10px;
	 }

	 .TaskTable td.parent {
	   padding: 0px 5px 0px 5px;
	   font-weight:normal;
	   font-size:10px;
	   height: 10px;
	 }

   </style>
  </head>
  <body>
  <xsl:for-each select="tasklist/task">
	<div class="TaskTable" >
	<table border="1">
	  <tr >
		<td class="id"><xsl:value-of select="id"/></td>
	  </tr>
	  <tr >
		<td class="name"><xsl:value-of select="name"/></td>
	  </tr>
	  <tr>
		<td class="empty"></td>
	  </tr>
	  <tr >
		<td class="projects">Projects:<xsl:value-of select="projects" /></td>
	  </tr>
	  <tr >
		<td class="parent">Parent:<xsl:value-of select="parent"/></td>
	  </tr>
	</table>
	</div>
  </xsl:for-each>
  </body>
  </html>
  </xsl:template>
 </xsl:stylesheet>
 <tasklist>
"""

xml_footer="""
</tasklist>
</doc>
"""

with open(sys.argv[1], 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	line_idx=0
	print xml_header
	for row in reader:
		if line_idx==0:
			line_idx+=1
			continue
		else:
		    line_idx+=1
		taskid,createdat,completedat,lastmodified,name,assignee,duedate,tags,notes,projects,parenttask=row
		print "  <task>"
		print "    <id>"+taskid+"</id>"
		print "    <name>"+name+"</name>"
		print "    <projects>"+projects+"</projects>"
		print "    <parent>"+parenttask+"</parent>"
		print "  </task>"
	print xml_footer
