import microgear.client as microgear
import time
import os
import optimize_data_median_med_ewmaV3_2 as optimize

import db_mongo as db
# import trilaterlation as cal
# import math

appid = "seniorProject"
gearkey = "mS2SW6zylEzbpKg"
gearsecret =  "3gSQjYWs5nFBS3WxyEqaQTwOO"

""" function send data to mongo database """
#set grobal "dic" is data for send to database

dic = {}
dic_station ={}
period = 0

# db.APsList()


def RSSIroomTagToAP(message,number):
	# print  message,number
	if message == "<":
		dic_station.clear()
	elif message == ">":
		optimize.searchAP(dic_station,number)
		# optimize.reset_listAP()
	else:
		#split
		data2 = message.split(",")
		#add to dic
		dic_station[data2[1]] = data2[2]

def RSSImotagToAll(message,number):
	# print  message
	# global period
	data_return = ''
	if message == "<":
		# print "start"
		dic.clear()
	elif message == ">":
		
		optimize.searchALL(dic,number)



		#  	optimize.reset_list()
		# #send data to db_mongo.py function
		# # print dic
		
		# # print period
		# # cal.findap(dic)
		# #db.insert(dic)
	else:
		#split
		data = message.split(",")
		#add to dic
		dic[data[1]] = data[2]

microgear.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
  print "Now I am connected with netpie"

def subscription(topic,message):
	#print message
	#print topic
	if topic == "/seniorProject/data/1":
		RSSImotagToAll(message,1)
		# print	message
	elif topic == "/seniorProject/data/2":
		RSSImotagToAll(message,2)
	elif topic == "/seniorProject/data/3":
		RSSImotagToAll(message,3)
	elif topic == "/seniorProject/data/4":
		RSSImotagToAll(message,4)
	elif topic == "/seniorProject/Station_data/1":
		RSSIroomTagToAP(message,1)
	elif topic == "/seniorProject/Station_data/2":
		RSSIroomTagToAP(message,2)
	elif topic == "/seniorProject/Station_data/3":
		RSSIroomTagToAP(message,3)
	elif topic == "/seniorProject/Station_data/4":
		RSSIroomTagToAP(message,4)
	elif topic == "/seniorProject/dataControl":
		print	message	
	else:
		# print message
		optimize.initial_Val(message)

def disconnect():
  print "disconnect is work"

def callback_present(gearkey) :
    print gearkey+" become online."

def callback_absent(gearkey) :
    print gearkey+" become offline."

microgear.setalias("Server")
microgear.on_present = callback_present
microgear.on_absent = callback_absent
microgear.on_connect = connection
microgear.on_message = subscription
microgear.on_disconnect = disconnect
microgear.subscribe("/data/1")
microgear.subscribe("/data/2")
microgear.subscribe("/data/3")
microgear.subscribe("/data/4")
microgear.subscribe("/Station_data/1")
microgear.subscribe("/Station_data/2")
microgear.subscribe("/Station_data/3")
microgear.subscribe("/Station_data/4")
microgear.subscribe("/dataControl")
# microgear.subscribe("/web")
os.system('rm microgear.cache')
#client.connect()
microgear.connect()

count_reset = 0
count_Notify = 0
db.APsList()

optimize.findAP()
optimize.findTagRoom()
optimize.findMoTag()
microgear.chat("WebServer","ready")


while(True):
	# optimize.call_checktime()
	# microgear.publish("/data","test")
	# optimize.trilateration(2.22478863989/5,7.89384797649/5,3.5261/5)
	# optimize.trilateration(5/5,7/5,5/5)
	# send = input("what word to send esp8266:")
	
	# microgear.chat("client_station",send)
	

	# ////////////////////////////////////////////////////////////
	# temp = optimize.compare()
	# optimize.resetALL()
	# # print temp
	# if temp[0] != "none":
	# 	microgear.chat(temp[0],temp[1])
	# 	if temp[1] == "ON":
	# 		count_Notify = count_Notify +1
	# 		if count_Notify >= 7:
	# 			optimize.Notify_Line()
	# 			count_Notify = 0
	# 	count_reset = 0
	# else:
	# microgear.chat("test","ok Done")
	# 	count_reset = count_reset +1 
	# 	if count_reset > 5:
	# microgear.chat("WebServer","0000000")
	# 		optimize.resetALL()
	# print optimize.getData()
	# 		count_reset = 0
	time.sleep(1)
	