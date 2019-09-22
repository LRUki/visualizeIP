from ipAnalyze import organize
from ipAnalyze import visualize as vs
from ipAnalyze import gMap
import json


import os
path_to_data = os.getcwd()+"/ip.json"
organizeData = organize.organizeIpInfo(path_to_data)


#raw data
print('Collected raw data in ip.json file: ')
for obj in organizeData.data[:3]+organizeData.data[-3:]:
	print(json.dumps(obj,indent=2))

#summary of the data
print('summary of the data:')
print(organizeData.summary())
#print('\n')

'''visualization of the data'''

#pie chart: displays the percentage of the numOfIp/region/city by country and numOfIp by region/city
countryDf,regionDf,cityDf = organizeData.pandasDF()

vs.pie(dtype='numberOfIp',Df=countryDf)

#Overview of the data
#Displaying the top 1~20th countries
vs.barplot_Overview(index=[1,10],Df=countryDf)


#plot on gmap
Map = gMap.plotOnGMap(countryDf,regionDf)
Map.plotByCountries()
Map.plotByRegions()