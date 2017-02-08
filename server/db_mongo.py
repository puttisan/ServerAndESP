from pymongo import MongoClient

# con=MongoClient("localhost",27017)
con=MongoClient("128.199.119.31",27017)

stay=con.get_database("my-project")

myroom=stay.inmyroom


#myroom.insert(test)
def MotagList():
	list_re = []
	mymotag = stay.tags
	for a in mymotag.find():
		list_re.append(str(a['Tag_id']))
		# print list_re
	return list_re
def APsList():
	list_re = []
	myAP = stay.aps
	for a in myAP.find():
		list_re.append(str(a['AP_mac']))
	return list_re

def tagRoomList():
	list_re = []
	temp = 0
	mytagRoom = stay.rooms
	for a in mytagRoom.find():
		try:
			list_re.append([])
			list_re[temp].append(str(a['Room_mac']))
			list_re[temp].append(str(a['InitialValue']))
			temp = temp + 1
		except:
			print "out of mac"
	# print list_re
	return list_re


def insert(data):
	#data = {'test':'123','test2':'234'}
	myroom.insert(data)
	print "success add to mongo database"

def findid(Mac):
	myid = stay.rooms
	for a in myid.find({'Room_mac':Mac}):
		return a['Room_id'] 
