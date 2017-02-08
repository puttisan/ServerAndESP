# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 22:05:37 2016

@author: puttisan
"""

import math


def findDistanceformFSPL(RSSI):
    d =[]
    frequnce = [2.4,5.1,5.7]
    for f in frequnce :
        distance = math.pow(10,((float(RSSI)-(20*math.log10(f*math.pow(10,3)))+27.55)/20))
        d.append(distance)
    
    print d

while(1):
    RSSI = raw_input("put RSSI :")
    findDistanceformFSPL(RSSI)


