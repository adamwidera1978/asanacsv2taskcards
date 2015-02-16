#!/usr/bin/python
import csv
import sys
import time

#helper routines for estimating date periods
is_date_greater= lambda a,b: a.tm_year>b.tm_year or a.tm_mon>b.tm_mon or a.tm_mday>b.tm_mday
is_date_smaller= lambda a,b: b.tm_year>a.tm_year or b.tm_mon>a.tm_mon or b.tm_mday>a.tm_mday
is_date_equal= lambda a,b: a.tm_year==b.tm_year and a.tm_mon==b.tm_mon and a.tm_mday==b.tm_mday
is_date_greater_equal = lambda a,b: is_date_greater(a,b) or is_date_equal(a,b)
is_date_smaller_equal = lambda a,b: is_date_smaller(a,b) or is_date_equal(a,b)

start_date=time.strptime(sys.argv[2],"%Y-%m-%d")
end_date=time.strptime(sys.argv[3],"%Y-%m-%d")
filter_tag=""
if len(sys.argv)>4:
	filter_tag=sys.argv[4]

#Check if the given period is valid
if not is_date_greater(end_date,start_date):
	exit(1)

#Check the total number of work days within the period
days_count=0
tmp_date=start_date
while True:
	if tmp_date.tm_wday in range(0,5):
		days_count+=1
	tmp_date=time.localtime(time.mktime(tmp_date)+24*60*60)
	if (is_date_greater(tmp_date,end_date)):
	   break

with open(sys.argv[1], 'rb') as csvfile:
	total_points=0
	completed_points=0
	total_completed_points=0
	total_remaining_points=0
	delta_points=0
	
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	line_idx=0
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
		createdat=time.strptime(createdat,"%Y-%m-%d")
		if len(completedat):
			completedat=time.strptime(completedat,"%Y-%m-%d")
		else:
			completedat=None
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
			name=name[name.find(":")+1:].strip()
		if taskeffort is not None and taskeffort.isalnum() and filter_tag in tags:
			points=int(taskeffort)
			if is_date_greater_equal(createdat,start_date) and is_date_smaller_equal(createdat,end_date):
				delta_points+=points
			if completedat is not None:
				total_completed_points+=points
				if is_date_greater_equal(completedat,start_date) and is_date_smaller_equal(completedat,end_date):
					completed_points+=points
			total_points+=points
	total_remaining_points=total_points-total_completed_points
	print ",".join(map(lambda x:str(x),[days_count,total_points,completed_points,total_completed_points,total_remaining_points,delta_points]))
	
	
