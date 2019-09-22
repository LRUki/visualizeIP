#real
import time
import socket
import json
from pyipinfodb import pyipinfodb
from urllib.error import HTTPError 
import sys
import re
from datetime import datetime


# with open("/Users/Ryuta/more_ip.json","r") as f:
#     lineList=f.readlines()
# lastip=json.dumps(lineList[-9:-1],indent=2)
# print(lastip)
# pattern=re.compile(r"(\d{1,3}).(\d{1,3}).(\d{1,3}).0")
# results=re.search(pattern,lastip)
# X=int(results.group(1))
# Y=int(results.group(2))
# Z=int(results.group(3))
# print("Starting IP : {}.{}.{}.0 +1".format(X,Y,Z))

X,Y,Z=map(int,input("enter the first three digit:").split())


def writejson(path,type,data):
    f = open(path,type)
    f.write(json.dumps(data, indent=2))
    f.write(",")
    f.close()
print("Starting time:{}".format(str(datetime.now())))


ip_if=pyipinfodb.IPInfo("c8825bed76ebd5569eea87a46a0e103b7f6de30335343702aadd9d4ebba95949")
for x in range(X,226):
    if x==10 or x==127:
            continue
    print(x)
    print(datetime.now())
    for y in range(0,256):
        if x==X:    #<-- collecting the appropriate data when resuming the code after being interrupted 
            y+=Y
            if y>255:
                break
        for z in range(0,6):  
            if x==X and y==Y:
                z+=int((Z/40)+1)    
                if z>5:
                    break
            time.sleep(0.5)
            if (x==172 and y>=16 and y<=31) or (x==192 and y==168):
                continue
            try:
                eachdata=ip_if.get_city("{}.{}.{}.0".format(x,y,z*40))  #1.0.0.0 ～ 226.255.200.0
            except socket.gaierror:    #to make the program continue even if the ip address does not exist
                continue
            except HTTPError:                  
                time.sleep(0.5)
                eachdata=ip_if.get_city("{}.{}.{}.0".format(x,y,z*40))
            except ConnectionResetError:
                time.sleep(0.5)
                eachdata=ip_if.get_city("{}.{}.{}.0".format(x,y,z*40))
            except:
                print("Ending time:{}".format(str(datetime.now())))
                sys.exit("The last address saved:{}.{}.{}.0".format(x,y,(z-1)*40))
            if eachdata["countryName"]=="-" or len(eachdata["countryName"])==0:
                print("None")
                continue 
            datadic={"ipAddress":eachdata["ipAddress"],"countryName":eachdata["countryName"],
                 "cityName":eachdata["cityName"],"regionName":eachdata["regionName"],
                "latitude":eachdata['latitude'],"longitude":eachdata['longitude'],
                 "zipCode":eachdata['zipCode'],"timeZone":eachdata["timeZone"]}
            writejson("/Users/Ryuta/more_ip.json","a+",datadic)