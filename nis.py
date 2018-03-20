###########import###############
import json
import requests

###########global###############
read_count=0

def getTemperature():
	url = 'http://192.168.178.108:8080/Thingworx/Things/nectThing/Properties/Temperature'
	headers = {'appKey': 'c56e4f1b-d1d4-4f9d-ab20-0bf3c08dc363','Accept': 'application/json'}
	getreq = requests.get(url, headers=headers).json()
	s = getreq["rows"][0]["Temperature"]
	print(s)
	return s

while(read_count<100):
        x=getTemperature()
        f= open('readings.csv','a')
        f.write(str(x))
        f.close()
        read_count+=1
