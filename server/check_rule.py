import sched, time, calendar
import threading
import datetime
from pymongo import MongoClient
import requests,json
import microgear.client as microgear

client = MongoClient()
client = MongoClient('128.199.119.31', 27017)
db = client['my-project']
db_status = db.ifstatuses

url = "https://notify-api.line.me/api/notify"

'''---------------------------------
	lib line ** function then line
----------------------------------'''

def then_line(token,message):
	msg = {"message":message}
	LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+token}
	session = requests.Session()
	a=session.post(url, headers=LINE_HEADERS, data=msg)
	print(a.text)

'''---------------------------------
	Check date day time
----------------------------------'''

def check_date(date):
	rule = db.ifdates
	clear_status('date')
	cursor = rule.find({"ifDate_date":date})
	for document in cursor:
		print document
		db_status.update({'IfID':document['IfDate_id']},{'$set':{'IfDate':'1'}})
		check_status(str(document['IfDate_id']))

def check_day(day):
	rule = db.ifdays
	clear_status('day')
	cursor = rule.find({"ifDay_day":day})
	for document in cursor:
		db_status.update({'IfID':document['IfDay_id']},{'$set':{'IfDay':'1'}})
		check_status(str(document['IfDay_id']))

def check_minute(time):
	rule = db.iftimes
	clear_status('minute')
	# temp = rule.find({''})
	# print temp[0]
	cursor = rule.find({"IfTime_time":time})
	# cursor = rule.find({})
	for document in cursor:
		# print document
		db_status.update({'IfID':document['IfTime_id']},{'$set':{'IfTime':'1'}})
		check_status(str(document['IfTime_id']))

'''---------------------------------
	clear status *** set status to 0
----------------------------------'''
def clear_status(type):
	if (type == 'minute'):
		rule = db.iftimes
		cursor = rule.find({'IfTime':'1'})
		for document in cursor:
			db_status.update({'IfID':document['IfTime_id']},{'$set':{'IfTime':'0'}})
	elif (type == 'day'):
		rule = db.ifdays
		cursor = rule.find({'IfDay':'1'})
		for document in cursor:
			db_status.update({'IfID':document['IfDay_id']},{'$set':{'IfDay':'0'}})
	elif (type == 'date'):
		rule = db.ifdates
		cursor = rule.find({'IfDate':'1'})
		for document in cursor:
			db_status.update({'IfID':document['IfDate_id']},{'$set':{'IfDate':'0'}})

'''---------------------------------
	check status all = 1
	then check db then
----------------------------------'''

def check_status(id):
	document = db_status.find({'IfID':id})
	check = document[0]
	if (check['IfTime'] == '1' or check['IfTime'] == '-'):
		if (check['IfDay'] == '1' or check['IfDay'] == '-'):
			if (check['IfDate'] == '1' or check['IfDate'] == '-'):
				if (check['IfTag'] == '1' or check['IfTag'] == '-'):
					print 'check then'
					check_then(id)

'''---------------------------------
	function then
	find rule in db thenline , thencontrol
----------------------------------'''

def check_then(id):
	db_line = db.thenlines
	db_control = db.thencontrols
	# line
	cursor = db_line.find({'ThenLine_id':id})
	for document in cursor:
		print 'then line'
		print 'token :' + document['ThenLine_token'] + '   message : ' + document['ThenLine_message']
		then_line(document['ThenLine_token'],document['ThenLine_message'])
	# control
	cursor = db_control.find({'ThenControl_id':id})
	for document in cursor:
		print 'then control'
		then_control(document['ThenControl_Control_id'],document['ThenControl_status'])


'''---------------------------------
	check time every minute
	if 0:0 then check day and date
----------------------------------'''

def check_time_current():
	localtime   = time.localtime()
	date_current = time.strftime("%d/%m/%Y",localtime)
	time_current = time.strftime("%H:%M",localtime)
	day_current = calendar.day_name[datetime.date.today().weekday()]
	print time_current
	# if(time_current == '0:0'):
	check_date(date_current)
	check_day(day_current)
	check_minute(time_current)

#  use thread
def check_time_rule(): 
    print "Check time rule..."
    check_time_current()
    threading.Timer(60, check_time_rule).start()


'''---------------------------------
	clear status for tag
	with old room
----------------------------------'''

def clear_status_tag(tagid):
	# print 'clear status tag ...'
	# print 'tagid : ' , tagid
	temp = db.tags.find_one({'Tag_id':int(tagid)})
	# print 'temp : ', temp
	if(temp != None):
		cursor = db.iftags.find({'IfTag_name':tagid , 'IfTag_room':temp['room']})
		for document in cursor:
			db_status.update({'IfID':document['IfTag_id']},{'$set':{'IfTag':'0'}})


'''---------------------------------
	check tag rule and set room in db_tag
	call from server
----------------------------------'''

def check_tag(tagid,inroomid):
	print tagid,inroomid
	db_tag = db.iftags
	clear_status_tag(tagid)
	db.tags.update({'Tag_id':int(tagid)},{'$set':{'room':(inroomid)}})
	cursor = db_tag.find({'IfTag_name':str(tagid) , 'IfTag_room':str(inroomid)})
	for document in cursor:
		print document
		db_status.update({'IfID':document['IfTag_id']},{'$set':{'IfTag':'1'}})
		check_status(document['IfTag_id'])

'''---------------------------------
	then Control 
	update db_control
----------------------------------'''

def then_control(id,status):
	# print int(id)
	# print status
	if(status=='on'):
		db.controls.update({'Control_id':int(id)},{'$set':{'Status':True}})
		print 'control id :' + str(id) + ' Status : True'
		#  do something .. netpie
		controlTag(int(id),True)
	else:
		db.controls.update({'Control_id':int(id)},{'$set':{'Status':False}})
		print 'control id :' + str(id) + ' Status : False'
		#  do something .. netpie
		controlTag(int(id),False)

def controlTag(number,Order_bool):
    send = ""
    if Order_bool is True:
        send = str(number) + "," + "ON"
        microgear.chat("client_Tag_control",send)
    elif Order_bool is False:
        send = str(number) + "," + "OFF"
        microgear.chat("client_Tag_control",send)

# def initial_value(RoomId,RSSI):
# 	db.rooms.update({'Room_id':int(RoomId)},{'$set':{'rssi':int(RSSI)}})
	
def returnChat(message):
	microgear.chat("WebServer",message)

# ----------------------   example    ------------------------------------------
		
check_time_rule()
# check_tag('-1','30')