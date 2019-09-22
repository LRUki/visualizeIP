#Organizing the data
import json
import numpy as np
import re
import pandas as pd
class organizeIpInfo():
    def __init__(self,fullpath):
        with open(fullpath) as f:
            jsondata = f.read()
        py_obj=json.loads(jsondata)
        self.data=[x for x in py_obj["data"] if (len(x["countryName"])>1 and len(x["regionName"])>1 and len(x["cityName"])>1)]  
        self.country,self.country_ipNum,self.country_coordinate=self.__country()
        self.country_city,self.city_ipNum,self.numberOfCities=self.__region_city("cityName")
        self.country_region,self.region_ipNum,self.numberOfRegions,self.region_coordinate=self.__region_city("regionName")
        
    
    def __country(self):
        data=np.array([x["countryName"] for x in self.data])
        c,indices,num=np.unique(data,return_index=True,return_counts=True)
        cor=[(x["latitude"],x["longitude"]) for x in np.array(self.data)[indices.data]]
        return list(c),list(zip(c,num)),list(zip(c,cor))
    
    def __region_city(self,column):
        dic={}
        data=[x[column]+"_"+x["countryName"] for x in self.data]
        c,indices,num=np.unique(data,return_index=True,return_counts=True)
        ip_num=list(zip(c,num))
        if column=="regionName":
            reg_cor=[(self.data[i]["latitude"],self.data[i]["longitude"]) for i in list(indices)]
            reg_cor=list(zip(c,reg_cor))
        for i,n in zip(indices,num):
            d=self.data[i]
            con=d["countryName"]
            col=d[column]
            try:
                dic[con].append(col)
                continue
            except KeyError:
                dic[con]=[]
                dic[con].append(col)                    
        if column=="regionName":
            return dic, ip_num, len(ip_num),reg_cor
        else:
            return dic, ip_num, len(ip_num)
    #pass in the dataName and dataType
    def extract_info(self,dtype,name):
        return list(filter(lambda d:d[dtype]==name,self.data))

    #pass in the countryName and returns the regions
    def extract_region(self,country):
        try:
            return self.country_region[country]
        except KeyError:
            print("Incorrect country name")
    #pass in the countryName and returns the cities
    def extract_city(self,country):
        try:
            return self.country_city[country]
        except KeyError:
            print("Incorrect country name")

    #below are the functions that can be used
    def summary(self):
        print("The total number of valid Data: "+str(len(self.data)))
        print("The total number of the countries included in the data: "+str(len(self.country)))
        print("The total number of the regions included in the data: "+str(self.numberOfRegions))
        print("The total number of the cities included in the data: "+str(self.numberOfCities))
        
    def check_ip(self,name,dtype="country"):
        replace={"country":"countryName","region":"regionName","city":"cityName"}[dtype]
        ip_list=list(filter(lambda d:d[replace]==name,self.data))
        return [x["ipAddress"] for x in ip_list if x[replace]!="-"]

    #pass in list with [[string,int],[string,int]...] format and return the sorted version
    def sort(self,lis):
        return sorted(lis,key=lambda contents:contents[1],reverse=True)
   

    def search(self,inp,name):
        data = dict(Country=self.country,Region=self.country_region,City = self.country_city)
        chosenData = str(data[name.capitalize()])
        self.inp=self.inp.capitalize()
        x = re.findall("[self.inp]")
    def pandasDF(self):	
        countryDF=pd.DataFrame({"countryName":self.country,
"numberOfIp":[x[1] for x in self.country_ipNum],
"numberOfRegion":[len(self.extract_region(x)) for x in self.country],
"numberOfCity":[len(self.extract_city(x)) for x in self.country],
"latitude":[float(x[1][0]) for x in self.country_coordinate],
                                "longitude":[float(x[1][1]) for x in self.country_coordinate]})
    
        countryDF = countryDF.sort_values(by="numberOfIp",ascending=False)	
        countryDF = countryDF[["countryName","latitude","longitude","numberOfIp","numberOfRegion","numberOfCity"]]

        regionDF=pd.DataFrame({"regionName":[x[0] for x in self.region_ipNum],
                            "numberOfIp":[x[1] for x in self.region_ipNum],
                            "latitude":[float(x[1][0]) for x in self.region_coordinate],
                            "longitude":[float(x[1][1]) for x in self.region_coordinate]})
        
        regionDF = regionDF[["regionName","latitude","longitude","numberOfIp"]]
        regionDF = regionDF.sort_values(by="numberOfIp",ascending=False)

        cityDF=pd.DataFrame({"cityName":[x[0] for x in self.city_ipNum ],
                            "ipNumber":[x[1] for x in self.city_ipNum]})
        cityDF=cityDF.rename(columns={"ipNumber":"numberOfIp"})
        cityDF=cityDF.sort_values(by="numberOfIp",ascending=False)
        return countryDF,regionDF,cityDF
    


