# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 09:48:17 2016

@author: puttisan
"""
import math
import random
import numpy as np
import time
import httplib, urllib  
import requests,json
# import urllib.parse
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

import db_mongo as db


# data =[]
# data.append(0)
# data.append(0)
# data.append([])
# data.append([])
# data.append([])

# dataAP =[]
# dataAP.append(-43)

AP =[]
tagRoom =[]
tagRoomData = []
beforeAP = []
set_beforeAP = []
count_resetAP = []
def findAP():
    global AP,tagRoomData
    AP = db.APsList()
    print AP

def findTagRoom():
    global tagRoom,tagRoomData,beforeAP,set_beforeAP,count_resetAP
    tagRoom = db.tagRoomList()
    print tagRoom
    a = len(tagRoom)
    for i in range (0,a):
        tagRoomData.append(0)
        beforeAP.append(-45)
        set_beforeAP.append(True)
        count_resetAP.append(0)
    # print tagRoomData 



data = []
count_reset = []
set_before = []
set_ESP =[]
before = []
def findMoTag():
    global data,count_reset,set_before,set_ESP
    motag = db.MotagList()
    # print motag
    for i in range(0,len(motag)):
        data.append([])
        count_reset.append([])
        set_before.append([])
        before.append([])
        set_ESP.append([])
        for j in range(0,len(tagRoom)):
            data[i].append(0)
            count_reset[i].append(True)
            set_before[i].append(True)
            before[i].append(-45)
            set_ESP[i].append(False)
    # print   data,count_reset,set_ESP,set_before



# dataAP.append([])
# dataAP.append([])
# dataAP.append([])

# data_ewma =[]
# data_ewma.append([])
# data_ewma.append([])
# data_ewma.append([])




# 2.22478863989
# 7.89384797649
# 3.5261

# print data
# 0021297ED23A --> linksys-cisco
# 10BEF57597C8 --> linksys-PJEND
# 002275D13D64 --> Belkin
# 1CAFF7B6A392 --> Boardcom 
# 6E-25-B9-83-E8-40 --> vivo
# set_before = [True,True]
# set_beforeAP = [True]
# before = [-45,-45]

# list_AP = ["5ECF7F1AF2F8","54511BCCBAB4",""]
# list_AP = ["5ECF7F1AF2F8","DC094CF3ECFC",""]
# AP = ["54511BCCBAB4"]
# AP = ["DC094CF3ECFC"]
# list_AP = ["10BEF57597C8","002275D13D64","1CAFF7B6A392"]
# list_AP = ["10BEF57597C8","002275D13D64","0021297ED23A"]
# list_AP = ["10BEF57597C8","002275D13D64","6E25B983E840"]

# data[0].append(list_AP[0])
# data[1].append(list_AP[1])
# data[2].append(list_AP[2])
# set_AP = False
# set_ESP = [False,False]


def resetALL():
    global set_AP,set_ESP
    # reset_listAP()
    # reset_list()
    set_AP = False
    set_ESP = [False,False]



def checkAP():
    if not data[0] :
        return 1
    if not data[1] :
        return 1
    if not data[2] :
        return 1
    return 0 
def reset_list():
    del data[:]
    data.append([])
    data.append([])
    data.append([])

def reset_listAP():
    del dataAP[:]
    dataAP.append([])
    dataAP.append([])
    dataAP.append([])


def searchAP(dic,number):
    global beforeAP,count_resetAP,set_beforeAP,AP,tagRoomData
    number = number -1
    # print dic,number,tagRoom,tagRoomData,beforeAP,count_resetAP
    for i,j in dic.items():
        for a in range(0,len(AP)):
            if i == AP[a]:
                # print i,AP[a],number,j,beforeAP[number]
                # ewma_forward(before,j)
                # ewma_backward(before,j)
                # if ewma_forward
                # data[0].append(j)
                intitial_ewmaAP(j,number)
                # print "data 0 :",i

                # print "--------------------------------------------------------"
                # print j
                # print ewma_forward(beforeAP[0],j)
                # print ewma_backward(beforeAP[0],j)
                if int(ewma_backward(beforeAP[number],j) - ewma_forward(beforeAP[number],j)) in range(-5,5):
                    # dataAP[0].append(ewma_forward(beforeAP[0],j))
                    temp = ewma_forward(beforeAP[number],j)
                    tagRoomData[number] = temp
                    # SendDataToThingSpeak(int(ewma_forward(beforeAP[0],j)),3)
                    # print "RSSI station to ap: "+str(dataAP[0])
                    # print beforeAP[0]
                    beforeAP[number] =  temp
                    # print "Done3"
                else:
                    # print count_resetAP[0]
                    if count_resetAP[number] >= 3:
                        set_beforeAP[number] = True
                        count_resetAP[number] = 0
                    count_resetAP[number] = count_resetAP[number] + 1
def compare(number,dic,data,temp):
    # global data,dataAP,set_AP,set_ESP
    # print set_AP,set_ESP,data,dataAP
    # if checkTrue(number) == True :
        # APtoEsp = int(data[1])
        # APtoStation = int(dataAP[0])
        # EsptoStation = int(data[0])
        # print APtoEsp,APtoStation,EsptoStation
        # if abs(int(APtoEsp - APtoStation)) in range(0,7) and int(EsptoStation) >= -46 :
        #     return "client_station","ON"
        # else :
        #     # print APtoEsp,APtoStation,EsptoStation
        #     return "client_station","OFF"

        #     return True
        # else:
        #     return False
        
    # else :
    #     return "none","none"
    # print "do compare"
    # print number,dic,data,temp  
    for i,j in dic.items():
        # print "Do1"
        for a in range(0,len(AP)):
            # print "Do2",i,AP[a]
            if i == AP[a]:
                print "StaToAP",tagRoomData[temp],"EspToAP",j,"EspToSta",data
                # print number,dic,data,temp,i,j,tagRoomData[temp]
                SendDataToThingSpeak(j,6)
                time.sleep(5)
                SendDataToThingSpeak(tagRoomData[temp],7)
                time.sleep(5)
                SendDataToThingSpeak(data,8)
                if int(tagRoomData[temp]) != 0:
                    if abs(int(int(j)-int(tagRoomData[temp]))) in range(0,7) and int(data) >= -46:
                        print "Trun ON Light"
                    else:
                        print "Trun OFF Light"



def searchALL(dic,number):
    global before,count_reset,set_before,set_ESP
    # print dic
    number = number - 1
    for i,j in dic.items():
        for a in range(0,len(tagRoom)):
            if i == tagRoom[a]:
                # print i,AP[a],number,j,before[number][a]
                # if set_ESP[number][a] == False:
                    # ewma_forward(before,j)
                    # ewma_backward(before,j)
                    # if ewma_forward
                    # data[0].append(j)
                intitial_ewma(j,a,number)
                    # print "data 0 :",i

                    # print "--------------------------------------------------------"
                    # print j
                    # print ewma_forward(before[0],j)
                    # print ewma_backward(before[0],j)
                if int(ewma_backward(before[number][a],j) - ewma_forward(before[number][a],j)) in range(-5,5):
                        # data[0].append(ewma_forward(before[0],j))
                    temp = ewma_forward(before[number][a],j)
                    data[number][a] = temp
                        # SendDataToThingSpeak(int(ewma_forward(before[0],j)),1)
                        # print "ESP to station :"+str(data[0])
                        # print before[0]
                    before[number][a] =  temp
                    # print "okDone",dic
                    compare(number,dic,data[number][a],a)
                    # set_ESP[number][a] = True
                else:
                        # print count_reset[0]
                    if count_reset[number][a] >= 3:
                        set_before[number][a] = True
                        count_reset[number][a] = 0
                    count_reset[number][a] = count_reset[number][a] + 1

                

def checkTrue(number):       
    for i in range(0,len(set_ESP[number])):
        if set_ESP[number][i] == False:
            return False
    return True

def getData():
    return tagRoomData

def intitial_ewma(be,temp,number):
    global before,set_before
    if set_before[number][temp] == True:
        before[number][temp] = be
        set_before[number][temp] = False
def intitial_ewmaAP(be,temp):
    global beforeAP,set_beforeAP
    if set_beforeAP[temp] == True:
        beforeAP[temp] = be
        set_beforeAP[temp] = False
def ewma_forward(before,current):
    lamda = 0.75
    before = int(before)
    current = int(current)
    # print before,current,lamda
    return float((lamda*current)+(1-lamda)*before)
def ewma_backward(before,current):
    lamda = 0.25
    before = int(before)
    current = int(current)
    return float((lamda*current)+(1-lamda)*before)


def SendDataToThingSpeak(temp,field):
    filed_txt = 'field'+str(field)
    params = urllib.urlencode({filed_txt:temp,'key':'YJQGHUF4LJD7L307'}) 
    # use your API key generated in the thingspeak channels for the value of 'key'
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")  
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"
    # time.sleep(60)              #Delay 1 minute
def Notify_Line():
    # print "Do"
    LINE_ACCESS_TOKEN="9vUpN5JOYrSNlPRPLgxTYC1fKLYyjO9LWRukUvtujQU"
    url = "https://notify-api.line.me/api/notify"
     
     
    message ="บุคคลเออยู๋ในห้องนอนนานเกินไป" # ข้อความที่ต้องการส่ง
    # msg = urllib.parse.urlencode({"message":message})
    msg = urllib.urlencode({"message":message})
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    a=session.post(url, headers=LINE_HEADERS, data=msg)
    # print(a.text)