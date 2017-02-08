import microgear.client as microgear
import time
import os
import optimize_data_median_med_ewmaV2 as optimize

#import db_mongo as db
import trilaterlation as cal
# import math

appid = "seniorProject"
gearkey = "mS2SW6zylEzbpKg"
gearsecret =  "3gSQjYWs5nFBS3WxyEqaQTwOO"

""" function send data to mongo database """
#set grobal "dic" is data for send to database

dic = {}
dic_station ={}
period = 0
# Pt_a1 = 25  
# Pt_a2 = 33
# Pt_a3 = 50
Pt_a1 = 25
Pt_a2 = 33
Pt_a3 = 25
# Pt_a1 = 25
# Pt_a2 = 33
# Pt_a3 = 21
def senddatatoTS(message):
	if message == "<":
		dic_station.clear()
	elif message == ">":
		optimize.searchAP(dic_station)
		# optimize.reset_listAP()
	else:
		#split
		data = message.split(",")
		#add to dic
		dic_station[data[1]] = data[2]

def senddatatodb(message):
	# print  message
	# global period
	data_return = ''
	if message == "<":
		# print "start"
		dic.clear()
	elif message == ">":
		
		optimize.searchALL(dic)
		# print optimize.checkAP()
		# -----------------------------------------------------------work space (temporary comment)---------------------------------------------
		# if optimize.checkAP() == 0 :
		# 	print "AP_Dlink "+str(optimize.getData()[0])
		# 	print "AP_Belkin "+str(optimize.getData()[1])
		# 	print "AP_BoardCom "+str(optimize.getData()[2])
			

		# 	# print optimize.getData()
		# 	FSPL_ap_dlink = optimize.FreeSpacePathLoss(int(optimize.getData()[0][0]),2.4,Pt_a1)
		# 	FSPL_ap_belkin = optimize.FreeSpacePathLoss(int(optimize.getData()[1][0]),2.4,Pt_a2)
		# 	FSPL_ap_voardcom = optimize.FreeSpacePathLoss(int(optimize.getData()[2][0]),2.4,Pt_a3)

		# 	print "AP_Dlink_Distance "+str(FSPL_ap_dlink)
		# 	print "AP_Belkin_Distance "+str(FSPL_ap_belkin)
		# 	print "AP_BoardCom_Distance "+str(FSPL_ap_voardcom)


		# 	Position_tag = optimize.trilateration(FSPL_ap_dlink,FSPL_ap_belkin,FSPL_ap_voardcom)
		# 	print round(Position_tag[0]),round(Position_tag[1])
		# 	microgear.chat("htmlgear",str(round(Position_tag[0]))+","+str(round(Position_tag[1])))

			
			# optimize.reset_list()
		# else:
			# optimize.reset_list()

		# ----------------------------------------------------------------------------------------------------------------------
		# if period < 10:
		# 	optimize.seachAP(dic)
		# 	period += 1
		# else:
		#  	# data_return = optimize.getdata()

		#  	# data_return = optimize.ewma()
		#  	# print data_return
		#  	period = 0
		#  	print "data from AVG : "+str(optimize.AVG(optimize.getData()))
		#  	print "data from median : "+str(optimize.median(optimize.getData()))
		#  	print "data from AVG(ewma) : "+str(optimize.AVG(optimize.ewma()))
		#  	print "data from median(ewma) : "+str(optimize.median(optimize.ewma()))



		#  	FSPL_avg = [optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.getData())[1]),2.4,Pt_a1),optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.getData())[3]),2.4,Pt_a2),optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.getData())[5]),2.4,Pt_a3)]
		#  	FSPL_median = [optimize.FreeSpacePathLoss(int(optimize.median(optimize.getData())[1]),2.4,Pt_a1),optimize.FreeSpacePathLoss(int(optimize.median(optimize.getData())[3]),2.4,Pt_a2),optimize.FreeSpacePathLoss(int(optimize.median(optimize.getData())[5]),2.4,Pt_a3)]
		#  	FSPL_emwa_avg = [optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.ewma())[1]),2.4,Pt_a1),optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.ewma())[3]),2.4,Pt_a2),optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.ewma())[5]),2.4,Pt_a3)]
		#  	FSPL_ewma_median =[optimize.FreeSpacePathLoss(int(optimize.median(optimize.ewma())[1]),2.4,Pt_a1),optimize.FreeSpacePathLoss(int(optimize.median(optimize.ewma())[3]),2.4,Pt_a2),optimize.FreeSpacePathLoss(int(optimize.median(optimize.ewma())[5]),2.4,Pt_a3)]
		#  	print "\t\tDistance"
		#  	print "avg\t\tmedian\t\tewma avg\tewma median"
		#  	print  optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.getData())[1]),2.4,Pt_a1),optimize.FreeSpacePathLoss(int(optimize.median(optimize.getData())[1]),2.4,Pt_a1),optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.ewma())[1]),2.4,Pt_a1),optimize.FreeSpacePathLoss(int(optimize.median(optimize.ewma())[1]),2.4,Pt_a1)
		#  	print  optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.getData())[3]),2.4,Pt_a2),optimize.FreeSpacePathLoss(int(optimize.median(optimize.getData())[3]),2.4,Pt_a2),optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.ewma())[3]),2.4,Pt_a2),optimize.FreeSpacePathLoss(int(optimize.median(optimize.ewma())[3]),2.4,Pt_a2)
		#  	print  optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.getData())[5]),2.4,Pt_a3),optimize.FreeSpacePathLoss(int(optimize.median(optimize.getData())[5]),2.4,Pt_a3),optimize.FreeSpacePathLoss(int(optimize.AVG(optimize.ewma())[5]),2.4,Pt_a3),optimize.FreeSpacePathLoss(int(optimize.median(optimize.ewma())[5]),2.4,Pt_a3)
		#  	print "\n"


		#  	print "\t\t Position From Free Space Path loss"
		#  	print "avg filter"
		#  	print optimize.trilateration(float(FSPL_avg[0])/0.3,float(FSPL_avg[1])/0.3,float(FSPL_avg[2])/0.3)
		#  	print "median filter"
		#  	print optimize.trilateration(float(FSPL_median[0]/0.3),float(FSPL_median[1]/0.3),float(FSPL_median[2]/0.3))
		#  	print "ewma avg"
		#  	print optimize.trilateration(float(FSPL_emwa_avg[0]),float(FSPL_emwa_avg[1]),float(FSPL_emwa_avg[2]))
		#  	temp_x = optimize.trilateration(float(FSPL_emwa_avg[0]),float(FSPL_emwa_avg[1]),float(FSPL_emwa_avg[2]))[0]
		#  	temp_y = optimize.trilateration(float(FSPL_emwa_avg[0]),float(FSPL_emwa_avg[1]),float(FSPL_emwa_avg[2]))[1]
		#  	# microgear.chat("htmlgear",str(round(temp_x))+","+str(round(temp_y)))
		#  	print "ewma median"
		#  	print optimize.trilateration(float(FSPL_ewma_median[0]/0.3),float(FSPL_ewma_median[1]/0.3),float(FSPL_ewma_median[2]/0.3))


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
	if topic == "/seniorProject/data":
		senddatatodb(message)
		# print	message
	elif topic == "/seniorProject/Station_data":
		senddatatoTS(message)


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
microgear.subscribe("/data")
microgear.subscribe("/Station_data")
os.system('rm microgear.cache')
#client.connect()
microgear.connect()

count_reset = 0
count_Notify = 0
while(True):
	# microgear.publish("/data","test")
	# optimize.trilateration(2.22478863989/5,7.89384797649/5,3.5261/5)
	# optimize.trilateration(5/5,7/5,5/5)
	# send = input("what word to send esp8266:")
	# microgear.chat("esp8266",send)
	# microgear.chat("client_station",send)
	
	temp = optimize.compare()
	optimize.resetALL()
	# print temp
	if temp[0] != "none":
		microgear.chat(temp[0],temp[1])
		if temp[1] == "ON":
			count_Notify = count_Notify +1
			if count_Notify >= 7:
				optimize.Notify_Line()
				count_Notify = 0
		count_reset = 0
	else:
		count_reset = count_reset +1 
		if count_reset > 5:
			optimize.resetALL()
			count_reset = 0
	time.sleep(1)
	