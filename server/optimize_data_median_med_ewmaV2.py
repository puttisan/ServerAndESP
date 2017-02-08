# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 09:48:17 2016

@author: puttisan
"""
import math
import random
import numpy as np

import httplib, urllib  
import requests,json
# import urllib.parse
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse


data =[]
data.append(0)
data.append(0)
# data.append([])
# data.append([])
# data.append([])

dataAP =[]
dataAP.append(-43)
# dataAP.append([])
# dataAP.append([])
# dataAP.append([])

# data_ewma =[]
# data_ewma.append([])
# data_ewma.append([])
# data_ewma.append([])

count_reset = [0,0]
count_resetAP = [0]
# x1 = "3"
# y1 = "4"
# x2 = "1.5"
# y2 = "6"
# x3 = "3.2"
# y3 = "3.5"

x1 = "14"
y1 = "7"
x2 = "6"
y2 = "33"
x3 = "36"
y3 = "35"



# 2.22478863989
# 7.89384797649
# 3.5261

# print data
# 0021297ED23A --> linksys-cisco
# 10BEF57597C8 --> linksys-PJEND
# 002275D13D64 --> Belkin
# 1CAFF7B6A392 --> Boardcom 
# 6E-25-B9-83-E8-40 --> vivo
set_before = [True,True]
set_beforeAP = [True]
before = [-45,-45]
beforeAP = [-45]
# list_AP = ["5ECF7F1AF2F8","54511BCCBAB4",""]
list_AP = ["5ECF7F1AF2F8","DC094CF3ECFC",""]
# AP = ["54511BCCBAB4"]
AP = ["DC094CF3ECFC"]
# list_AP = ["10BEF57597C8","002275D13D64","1CAFF7B6A392"]
# list_AP = ["10BEF57597C8","002275D13D64","0021297ED23A"]
# list_AP = ["10BEF57597C8","002275D13D64","6E25B983E840"]

# data[0].append(list_AP[0])
# data[1].append(list_AP[1])
# data[2].append(list_AP[2])
set_AP = False
set_ESP = [False,False]


def resetALL():
    global set_AP,set_ESP
    # reset_listAP()
    # reset_list()
    set_AP = False
    set_ESP = [False,False]

def compare():
    global data,dataAP,set_AP,set_ESP
    # print set_AP,set_ESP,data,dataAP
    if set_ESP == [True,True] :
        APtoEsp = int(data[1])
        APtoStation = int(dataAP[0])
        EsptoStation = int(data[0])
        print APtoEsp,APtoStation,EsptoStation
        if abs(int(APtoEsp - APtoStation)) in range(0,7) and int(EsptoStation) >= -46 :
            return "client_station","ON"
        else :
            # print APtoEsp,APtoStation,EsptoStation
            return "client_station","OFF"

        #     return True
        # else:
        #     return False
        
    else :
        return "none","none"

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
    # del data_ewma[:]
    data.append([])
    data.append([])
    data.append([])

    # data_ewma =[]
    # data_ewma.append([])
    # data_ewma.append([])
    # data_ewma.append([])
    # # print data , data_ewma

# def intitialewma():
def reset_listAP():
    del dataAP[:]
    dataAP.append([])
    dataAP.append([])
    dataAP.append([])


def searchAP(dic):
    global beforeAP,count_resetAP,set_beforeAP,set_AP
    for i,j in dic.items():
        if i == AP[0]:
            if set_AP == False :
                # ewma_forward(before,j)
                # ewma_backward(before,j)
                # if ewma_forward
                # data[0].append(j)
                intitial_ewmaAP(j,0)
                # print "data 0 :",i

                # print "--------------------------------------------------------"
                # print j
                # print ewma_forward(beforeAP[0],j)
                # print ewma_backward(beforeAP[0],j)
                if int(ewma_backward(beforeAP[0],j) - ewma_forward(beforeAP[0],j)) in range(-5,5):
                    # dataAP[0].append(ewma_forward(beforeAP[0],j))
                    dataAP[0] = ewma_forward(beforeAP[0],j)
                    # SendDataToThingSpeak(int(ewma_forward(beforeAP[0],j)),3)
                    # print "RSSI station to ap: "+str(dataAP[0])
                    # print beforeAP[0]
                    beforeAP[0] =  ewma_forward(beforeAP[0],j)
                    set_AP = True
                else:
                    # print count_resetAP[0]
                    if count_resetAP[0] >= 3:
                        set_beforeAP[0] = True
                        count_resetAP[0] = 0
                    count_resetAP[0] = count_resetAP[0] + 1
                
def searchALL(dic):
    global before,count_reset,set_before,set_ESP

    for i,j in dic.items():

        if i == list_AP[0]:
            if set_ESP[0] == False:
                # ewma_forward(before,j)
                # ewma_backward(before,j)
                # if ewma_forward
                # data[0].append(j)
                intitial_ewma(j,0)
                # print "data 0 :",i

                # print "--------------------------------------------------------"
                # print j
                # print ewma_forward(before[0],j)
                # print ewma_backward(before[0],j)
                if int(ewma_backward(before[0],j) - ewma_forward(before[0],j)) in range(-5,5):
                    # data[0].append(ewma_forward(before[0],j))
                    data[0] = ewma_forward(before[0],j)
                    # SendDataToThingSpeak(int(ewma_forward(before[0],j)),1)
                    # print "ESP to station :"+str(data[0])
                    # print before[0]
                    before[0] =  ewma_forward(before[0],j)
                    set_ESP[0] = True
                else:
                    # print count_reset[0]
                    if count_reset[0] >= 3:
                        set_before[0] = True
                        count_reset[0] = 0
                    count_reset[0] = count_reset[0] + 1
                

        elif i == list_AP[1]:
            # data[1].append(j)
            if set_ESP[1] == False:

                intitial_ewma(j,1)
                # print "data 0 :",i

                # print "--------------------------------------------------------"
                # print j
                # print ewma_forward(before,j)
                # print ewma_backward(before,j)
                if int(ewma_backward(before[1],j) - ewma_forward(before[1],j)) in range(-5,5):
                    # data[1].append(ewma_forward(before[1],j))
                    data[1] = ewma_forward(before[1],j)
                    # SendDataToThingSpeak(int(ewma_forward(before[1],j)),2)
                    # print "ESP to AP :"+str(data[1])
                    # print before
                    before[1] =  ewma_forward(before[1],j)
                    set_ESP[1] = True
                else:
                    # print count_reset
                    if count_reset[1] >= 3:
                        set_before[1] = True
                        count_reset[1] = 0
                    count_reset[1] = count_reset[1] + 1
                # print "data 1 :",i
                set_ESP[1] = True
            


        # elif i == list_AP[2]:
            # data[2].append(j)
        # else:
        #     print count_reset
        #     if count_reset >= 5:
        #         set_before = True
        #         count_reset = 0
        #     count_reset = count_reset + 0.5
               
    # if periodic == 10:
    #     print data[0]
    #     print data[1]
    #     print data[2]
       
    # print data[1]
    # print data[2]
    # for i in list_AP:
    #     if Mac_come == i:
    #         for j in data[0]:
    #             if i == j:
    #                 # data[j].append(RSSI)
    #         return 1
    #     else:
    #         return 0 
    # print dic
        
def getData():
    return data

def AVG(data_s):
    avg_ap1 = 0
    avg_ap2 = 0
    avg_ap3 = 0
    for i in data_s[0]:
        avg_ap1 += int(i)
    avg_ap1 = avg_ap1 / len(data_s[0])

    for j in data_s[1]:
        avg_ap2 += int(j)
    avg_ap2 = avg_ap2 / len(data_s[1])

    for k in data_s[2]:
        avg_ap3 += int(k)
    avg_ap3 = avg_ap3 / len(data_s[2])


    return str(list_AP[0]),avg_ap1 ,str(list_AP[1]),avg_ap2,str(list_AP[2]),avg_ap3



# def AVG(data):
#     temp = 0 
#     for i in range(0,len(data)):
#         temp += data[i]
#     return temp / len(data)
def intitial_ewma(be,temp):
    global before,set_before
    if set_before[temp] == True:
        before[temp] = be
        set_before[temp] = False
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


def ewma():
    lamda = 0.25    #0.25
    # print data_ewma
    # print data
    # print len(data)
    for j in range(0,len(data)):
        # print j
        data_ewma[j].append(data[j][0])
    for i in range(0,len(data)):
        for k in range (1,len(data[i])):
            temp = data_ewma[i][k-1]
            data_ewma[i].append(round((lamda*int(data[i][k]))+(1-lamda)*int(temp),0))
    
    # EWMA_RSSI = (lamda*current)+(1-lamda)*before

    return data_ewma


def median(data_s):
    for i in data_s:    
        sorted(i)

    return str(list_AP[0]),data_s[0][len(data_s[0])/2] ,str(list_AP[1]),data_s[1][len(data_s[1])/2],str(list_AP[2]),data_s[2][len(data_s[2])/2]



def FreeSpacePathLoss(signal,frequency,Pt):
    # signal = 20log(d) + 20log(f) + 92.45   d in km , f in Ghz
    # 20log(d) = signal - 20log(f) - 92.45
    Pt = Pt * (-1)
    Pr = Pt - signal
    lam = 0.125
    d0 = 1
    expo = 1
    # print Pt,signal
    # print float(Pt)/float(signal)
    # PL = 10 * math.log10(float(Pt)/float(signal))
    # distance = math.pow(10,((-1*signal)-(20*math.log10(frequency))-92.45)/20)
    # distance = (math.pow(10,(signal-(20*math.log10((4*math.pi*d0)/lam))) * d0) / (10*expo))
    distance = math.pow(10,(Pr-(20*math.log10(frequency))-92.45)/20)  
    # distance = math.pow(10,(PL-(20*math.log10(frequency))-92.45)/20)
    # distance = math.pow(10,(Pr/20))
    return distance * 1000 


def trilateration(d_ap1,d_ap2,d_ap3):
    # 2A*X = B
    # X =0 
    # Y =0
    # d_ap1 = d_ap1/1.167
    # d_ap2 = d_ap2/1.167
    # d_ap3 = d_ap3/1.167
    # d_ap1 = d_ap1/0.25
    # d_ap2 = d_ap2/0.25
    # d_ap3 = d_ap3/0.25
    # test = np.matrix([[1,2],[3,4]])
    # print test
    # print d_ap1,d_ap2,d_ap3
    A = np.matrix([[float(x3)-float(x1),float(y3)-float(y1)],[float(x3)-float(x2),float(y3)-float(y2)]])
    B = np.matrix([[(math.pow(float(d_ap1),2)-math.pow(float(d_ap3),2))-(math.pow(float(x1),2)-math.pow(float(x3),2))-(math.pow(float(y1),2)-math.pow(float(y3),2))],[(math.pow(float(d_ap2),2)-math.pow(float(d_ap3),2))-(math.pow(float(x2),2)-math.pow(float(x3),2))-(math.pow(float(y2),2)-math.pow(float(y3),2))]])
    # po = np.matrix([[X],[Y]])
    # print A
    # print B
    invA = np.linalg.inv(A)
    # print test
    # print B
    # print invA
    po = invA.dot(np.divide(B,2))
    # print invA.dot(np.divide(B,2))
    # po = B/2 * invA 
    # print po
    # po = np.divide(po,1000)
    return po
# data2 = []
# ref =[]
# temp1 =0
# temp2 =0
# temp3 =0

# temp5 =0
# for k in range(0,20):
#     data2.append([])
#     ref.append(random.randrange(39,51))
#     for m in range(0,20):
#         data2[k].append(random.randrange(39,51))

        
# temp4 = math.fabs(ewma(AVG(data2[0]),AVG(data2[1]))-ref[0])
# for h in range(0 , 20):
#     temp1 += math.fabs(AVG(data2[h])-ref[h]) 
#     if (h > 0 and h < 19):
#         #print h
#         temp4 += math.fabs(ewma(AVG(data2[h]),AVG(data2[h+1]))-ref[h])
#     print 'AVG : '+str(AVG(data2[h])) 
    


# for z in range(1,20):
#     temp2 += math.fabs(ewma(AVG(data2[z-1]),AVG(data2[z]))-ref[z])
#     #temp4 += math.fabs(ewma(AVG(data2[z-1]),AVG(data2[z]))-ref[z])  
#     print 'ewma : '+str(ewma(AVG(data2[z-1]),AVG(data2[z])))
    
# temp5 = math.fabs(ewma(AVG(data2[0]),AVG(data2[1]))-ref[0])
# for t in range(0 , 20):
#     if (t > 0 and t < 19):
#         temp5 += math.fabs(ewma(median(data2[t]),median(data2[t+1]))-ref[t])
#     temp3 += math.fabs(median(data2[t])-ref[t])
#     print 'med : '+str(median(data2[t]) )
    
    
# print 'err : AVG : '+str(temp1)
# #print 'err : ewma : '+str(temp2)
# print 'err : median : '+str(temp3)
# print 'err : ewma->AVG : '+str(temp4)
# print 'err : ewma->Median : '+str(temp5)
    
    
#print data2[0][0]-ref[0]
#for j in range(0,len(data)):

#    temp +=  float(data[j])
    
#print 'avg '+str(temp/len(data))+'\n'

#for i in data:
#    ewma(float(i),float(i)+1)
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
    print "Do"
    LINE_ACCESS_TOKEN="9vUpN5JOYrSNlPRPLgxTYC1fKLYyjO9LWRukUvtujQU"
    url = "https://notify-api.line.me/api/notify"
     
     
    message ="บุคคลเออยู๋ในห้องนอนนานเกินไป" # ข้อความที่ต้องการส่ง
    # msg = urllib.parse.urlencode({"message":message})
    msg = urllib.urlencode({"message":message})
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    a=session.post(url, headers=LINE_HEADERS, data=msg)
    print(a.text)