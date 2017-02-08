import microgear.client as microgear
import time
import os
# import optimize_data_median_med_ewma as optimize



appid = "seniorProject"
gearkey = "LoGZx3323O7Piql"
gearsecret =  "1XvHQPeUXnvVe5iPvJJnQw6Si"

microgear.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
  print "Now I am connected with netpie"

def subscription(topic,message):
  #print topic+" "+message
  print message

def disconnect():
  print "disconnect is work"

def callback_present(gearkey) :
    print gearkey+" become online."

def callback_absent(gearkey) :
    print gearkey+" become offline."

microgear.setalias("Client")
microgear.on_present = callback_present
microgear.on_absent = callback_absent
microgear.on_connect = connection
microgear.on_message = subscription
microgear.on_disconnect = disconnect
microgear.subscribe("/data")
os.system('rm microgear.cache')
#client.connect()
microgear.connect()

a = "E46F1361640A,-55,E46F13612900,-79,84C9B2A4DC59,-89,6C198F0CF97A,-90,6C198F0CF8FE,-84,48EE0C409820,-83,D4612E8A41C8,-88,048D388B78A3,-92,84C9B2A4DC58,-90,EC086B9BF001,-57,94FBB270D170,-37,A42BB0FD1059,-79,C83A350C8FB8,-84,28285DCFFDE8,-91,EC086B9C2172,-88,14D64D8E6DDC,-79,"
# a = "aaaaaa,-55,bbbbbb,-43,cccccc,-43,dddddd,-53,cccccc,-60,eeeeee,-49,ffffff,-50,gggggg,-39,hhhhhh,-45"

while(True):
	
	# microgear.publish("/data",a)
	time.sleep(10)