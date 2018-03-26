#!usr/bin/env python
###########import###############
import json
import requests
import time
###########global###############
read_count=0
sleep_time=1



##########functions#############
def getTemperature():
	url = 'http://192.168.178.108:8080/Thingworx/Things/nectThing/Properties/Temperature'
	headers = {'appKey': 'c56e4f1b-d1d4-4f9d-ab20-0bf3c08dc363','Accept': 'application/json'}
	getreq = requests.get(url, headers=headers).json()
	s = getreq["rows"][0]["Temperature"]
	print(s)
	return s

def getTrigger():
        f= open('/var/www/html/nectmatic/py_nis/nis.csv','r')
        z = f.readline()
        f.close()
        return z

def resetTrigger():
        f= open('/var/www/html/nectmatic/py_nis/nis.csv','w')
        f.write('0')
        f.close()
        
############main#############
try:
        while(True):
                while((read_count<100) & (getTrigger()=='1')):
                        x=getTemperature()
                        f= open('/var/www/html/nectmatic/simfiles/readings.csv','a')
                        f.write(str(x) + '\n')
                        f.close()
                        print(read_count)
                        read_count+=1
                        time.sleep(sleep_time)
                        if(read_count==99):
                                print('reset')
                                resetTrigger()
except (RuntimeError,TypeError,ValueError):
        print('Value Import Failed')
        
