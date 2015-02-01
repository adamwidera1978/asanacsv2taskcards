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
	   border:2px solid #AAAAAA;
	   page-break-inside: avoid !important;
	 }.TaskTable table{
		 border-collapse: collapse;
			 border-spacing: 0;
	   width:100%;
	   height:100%;
	   margin:0px;padding:0px;
	 }.TaskTable tr:hover td{
	   background-color:#ffffff;
	 }
	 .TaskTable td{
	   vertical-align:middle;
	   background-color:#ffffff;
	   border:0px solid #AAAAAA;
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
	   background-color:#AAAAAA;
	   border:0px solid #AAAAAA;
	   text-align:center;
	   border-width:0px 0px 0px 0px;
	   font-size:14px;
	   font-family:Arial;
	   font-weight:bold;
	   color:#ffffff;
	 }
	 .TaskTable tr:first-child:hover td{
	   background-color:#AAAAAA;
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

	 .TaskTable td.priority {
	   padding: 5px 5px 5px 5px;
	   font-weight:normal;
	   font-size:10px;
	   height: 12px;
	   width: 10%
	 }

	 .TaskTable td.severity {
	   padding: 5px 5px 5px 5px;
	   font-weight:normal;
	   font-size:10px;
	   height: 12px;
	   width: 10%
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

	 .TaskTable td.effort {
	   padding: 0px 5px 0px 5px;
	   font-weight:normal;
	   font-size:20px;
	   text-align:right;
	   color:#888;
	   height: 20px;
	 }

	 .TaskTable td.parent {
	   padding: 0px 5px 0px 5px;
	   font-weight:normal;
	   font-size:10px;
	   height: 10px;
	 }
	 div.whitebadge{
	   border: 0px solid;
	   border-radius: 12px;
	   background:white;
	   padding:2px;
	   margin:0px;
	   font-weight:bold;
	   color:#000;
	}

	.TaskTableGreen {
	   border-color:#37B30D;
	 }
	 .TaskTableGreen td{
	   border-color:#37B30D;
	 }
	 .TaskTableGreen tr:first-child td{

	   background-color:#37B30D;
	   border-color:#37B30D;
	 }
	 .TaskTableGreen tr:first-child:hover td{
	   background-color:#37B30D;
	 }


	 .TaskTableOrange {
	   border-color:#FF8000;
	 }
	 .TaskTableOrange td{
	   border-color:#FF8000;
	 }
	 .TaskTableOrange tr:first-child td{

	   background-color:#FF8000;
	   border-color:#FF8000;
	 }
	 .TaskTableOrange tr:first-child:hover td{
	   background-color:#FF8000;
	 }

	 .TaskTableYellow {
	   border-color:#FFD527;
	 }
	 .TaskTableYellow td{
	   border-color:#FFD527;
	 }
	 .TaskTableYellow tr:first-child td{

	   background-color:#FFD527;
	   border-color:#FFD527;
	 }
	 .TaskTableYellow tr:first-child:hover td{
	   background-color:#FFD527;
	 }

	 .TaskTableRed {
	   border-color:#FF0000;
	 }
	 .TaskTableRed td{
	   border-color:#FF0000;
	 }
	 .TaskTableRed tr:first-child td{

	   background-color:#FF0000;
	   border-color:#FF0000;
	 }
	 .TaskTableRed tr:first-child:hover td{
	   background-color:#FF0000;
	 }

	 .TaskTableBlue {
	   border-color:#007FFF;
	 }
	 .TaskTableBlue td{
	   border-color:#007FFF;
	 }
	 .TaskTableBlue tr:first-child td{

	   background-color:#007FFF;
	   border-color:#007FFF;
	 }
	 .TaskTableBlue tr:first-child:hover td{
	   background-color:#007FFF;
	 }

   </style>
  </head>
  <body>
  <xsl:for-each select="tasklist/task">
	 <div>
		<xsl:choose>
  			<xsl:when test='type = "PBI"'>
				<xsl:attribute name="class">TaskTable TaskTableOrange</xsl:attribute>
  			</xsl:when>
  			<xsl:when test='type = "DOC"'>
  				 <xsl:attribute name="class">TaskTable TaskTableGreen</xsl:attribute>
  			</xsl:when>
  			<xsl:when test='type = "DEV"'>
  				 <xsl:attribute name="class">TaskTable TaskTableBlue</xsl:attribute>
  			</xsl:when>
  			<xsl:when test='type = "QA"'>
  				 <xsl:attribute name="class">TaskTable TaskTableYellow</xsl:attribute>
  			</xsl:when>
  			<xsl:when test='type = "BUG"'>
  				 <xsl:attribute name="class">TaskTable TaskTableRed</xsl:attribute>
  			</xsl:when>
  			<xsl:otherwise>
				<xsl:attribute name="class">TaskTable</xsl:attribute>
  			</xsl:otherwise>
		</xsl:choose>

		<table border="1">
	  <tr >
		<td class="priority"><div class="whitebadge"><xsl:value-of select="priority"/></div></td>
		<td class="id"><xsl:value-of select="id"/></td>
		<td class="severity"><div class="whitebadge"><xsl:value-of select="severity"/></div></td>
	  </tr>
	  <tr >
		<td colspan="3" class="name" ><xsl:value-of select="name"/></td>
	  </tr>
	  <tr>
		<td colspan="3" class="empty"></td>
	  </tr>
	  <tr >
		<td colspan="2" class="projects">Projects:<xsl:value-of select="projects" /></td>
		<td rowspan="2" class="effort"><xsl:value-of select="effort"/></td>
	  </tr>
	  <tr >
		<td colspan="2" class="parent">Parent:<xsl:value-of select="parent"/></td>
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
		tasktype=None
		taskpriority=None
		taskseverity=None
		taskeffort=None
		if ((name.upper().startswith("BUG") or  
		name.upper().startswith("QA") or 
		name.upper().startswith("PBI") or
		name.upper().startswith("DOC") or 
		name.upper().startswith("DEV") or 
		name.upper().startswith("BUG") ) and (name.find(":") >= 0)) :
			if name.upper().startswith("BUG"):
				tasktype="BUG"
			if name.upper().startswith("PBI"):
				tasktype="PBI"
			elif name.upper().startswith("QA"):
				tasktype="QA"
			elif name.upper().startswith("DOC"):
				tasktype="DOC"
			elif name.upper().startswith("DEV"):
				tasktype="DEV"
			elif name.upper().startswith("BUG"):
				tasktype="BUG"
			if name.find("<")>=0 and name.find(">")>=0:
				taskpriority=name[name.find("<")+1:name.find(">")]
			if name.find("(")>=0 and name.find(")")>=0:
				taskseverity=name[name.find("(")+1:name.find(")")]
			if name.find("[")>=0 and name.find("]")>=0:
				taskeffort=name[name.find("[")+1:name.find("]")]	
			name=name[name.find(":")+1:]
		print "  <task>"
		print "    <id>"+taskid+"</id>"
		if tasktype is not None:
			print "    <type>"+tasktype+"</type>"
		if taskpriority is not None:
			print "    <priority>"+taskpriority+"</priority>"
		if taskseverity is not None:
			print "    <severity>"+taskseverity+"</severity>"
		if taskeffort is not None:
			print "    <effort>"+taskeffort+"</effort>"
		print "    <name>"+name+"</name>"
		print "    <projects>"+projects+"</projects>"
		print "    <parent>"+parenttask+"</parent>"
		print "  </task>"
	print xml_footer
