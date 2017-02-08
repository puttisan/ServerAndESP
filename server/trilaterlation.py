import math
import numpy

# ap1 = "003A99403EF0"
# ap1_x = 21.00
# ap1_y = 11.00
# ap2 = "0CF5A4419610"
# ap2_x = 19.50
# ap2_y = 7.00
# ap3 = "E0D1731A9983"
# ap3_x = 9.00
# ap3_y = 7.50
# ap4 = "84802DAB4ECF"
# ap4_x = 16.00
# ap4_y = 15.00

ap1 = "A42BB0BB28BD"
ap1_x = 21.00
ap1_y = 11.00
ap2 = "eeeeee"
ap2_x = 19.50
ap2_y = 7.00
ap3 = "ffffff"
ap3_x = 9.00
ap3_y = 7.50

# listap = {ap1:{"x":ap1_x,"y":ap1_y},ap2:{"x":ap2_x,"y":ap2_y},ap3:{"x":ap3_x,"y":ap3_y},ap4:{"x":ap4_x,"y":ap4_y}}
listap = {ap1:{"x":ap1_x,"y":ap1_y},ap2:{"x":ap2_x,"y":ap2_y},ap3:{"x":ap3_x,"y":ap3_y}}



dic = {"003AA99403EF0":"20","test":"30"}

#find minimum 3 range into dic and we have
def findap(dic):
	listap_have = []
	rssi = []
	for i,j in listap.items():
		for m,n in dic.items():
			if i == m:
				listap_have.append(listap[i]["x"])
				listap_have.append(listap[i]["y"])
				listap_have.append(fsbl(n))
				rssi.append(n)
			# print m,n,i,j
	# print listap_have
	#print rssi
	# print listap
	trilaterlation(listap_have)

#function free space pass lost
def fsbl(RSSI):
	distance = 0
	return distance
#write function matrix
def trilaterlation(data):
	print data[0]
	

if __name__ == "__main__":
    findap(dic)
    #print abs(-2)
    #print math.pow(2,2)