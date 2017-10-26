import requests
import os
import json
import time
import sys

##DataZone

urltable = []
x = 0
y = 0
inputbool = True
try:
	googleapiKeyfile = open("googleapiKey","r",encoding="UTF-8")
except:
	googleapiKeyfile = open("googleapiKey","w+",encoding="UTF-8")
keyString = googleapiKeyfile.readline()
googleapiKeyfile.close()

print("\n\nPlease KeyIn your Command")
print("\"REwrite\" for Override your GoogleApiKey or Press ENTER to Pass")
print("Now Your GoogleKey is "+keyString)
print("================================")

CommandCode = input()
if CommandCode == "REwrite" or keyString == "":
	googleapiKeyfile = open("googleapiKey","w",encoding="UTF-8")
	print("\n\nPlease KeyIn your GoogleApi Key")
	googleapiKeyfile.write(input())
	googleapiKeyfile.close()		

print("\n\nPlease drag Your datafile into this commandline")
rawinputName = input()

filename = rawinputName.split(" ")
print(filename[0])
file = open(filename[0],"r",encoding="UTF-8")
a = file.read()
file.close()

rawtable = a.split("\n")
rawtableX = len(rawtable)

while x < rawtableX:
	urltable.append(rawtable[x].split(","))
	x += 1

rowNumber = len(urltable)
lenNumber = len(urltable[0])

writefileB = open("dataoutput.csv","w",encoding="UTF-8")

googleapiKeyfile = open("googleapiKey","r",encoding="UTF-8")
keyString = googleapiKeyfile.readline()
googleapiKeyfile.close()


urllocation = -1
while y < rowNumber and urllocation < 0:
	for z in range(lenNumber-1):
		if urltable[y][z].find("goo.gl") > 0:
			urllocation = z
			break
	y += 1

for z in range(lenNumber):
	print(str(z) + "."+ urltable[0][z])

dataTable = ["序號","描述","GoogleUrl","點擊量","創造日期","計算日期","備註"]

while inputbool:
	print("Please Point out your Description row")
	print("================================")
	deslocation = input()
	try:
		int(deslocation) / 1 
	except:
		inputbool = True
	else:
		if int(deslocation) < lenNumber:
			inputbool = False

y = 0

while y < rowNumber:
	print("checking " + urltable[y][1])
	for z in range(len(dataTable)):

##拿到GoogleKey
		seekingurl = urltable[y][urllocation]
		googleapiKey = keyString
		httplinkurl = "https://www.googleapis.com/urlshortener/v1/url?key="+googleapiKey+"&shortUrl="+seekingurl+"&projection=FULL"

		data_jason = requests.get(httplinkurl)
		doc = json.loads(data_jason.content)

		try:
			doc["analytics"]
		except:
			if y > 0:
				print("Google APi Key make this ERROR\nPlease REwrite your Key");
				googleapiKeyfile = open("googleapiKey","w",encoding="UTF-8")
				googleapiKeyfile.write("")
				sys.exit()
		else:
			pass

##創作DataTable
		if y == 0:
			writefileB.write(dataTable[z])
		if z == 0 and y > 0:
			writefileB.write(str(y))
		if z == 1 and y > 0:
			writefileB.write(urltable[y][int(deslocation)])
		if z == 2 and y > 0:
			writefileB.write(seekingurl)
		if z == 3 and y > 0:
			writefileB.write(doc["analytics"]["allTime"]["shortUrlClicks"])
		if z == 4 and y > 0:
			dayRaw =doc["created"]
			dayDay = dayRaw.split("T")[0].split("-")
			dayTime = dayRaw.split("T")[1].split(".")[0].split(":")
			writefileB.write(dayDay[0] + "/" + dayDay[1] + "/" + dayDay[2] + " " + dayTime[0] + ":" + dayTime[1])

		if z == 5 and y > 0:
			writefileB.write(time.strftime("%Y/%m/%d %H:%M"))

		writefileB.write(",")
	writefileB.write("\n")
	y += 1

writefileB.close()
