# Australian Energy Market Operator (AEMO) half hourly Spot Price and Demand data script
# Released as open source and developed by Dr Liam Wagner, http://www.liamwagner.com/
# liam dot wagner at gmail dot com
# http://github.com/ldw77/Energy-Data/

# All data downloaded by this script is provided copyright free by AEMO http://www.aemo.com.au
# The first regions to enter the National Electricity Market were New South Wales, Queensland, Victoria, 
# South Australia and Snowy in December 1998. Following the interconnection of Victoria with Tasmina 
# via an undersea cable in May 2005. Snowy as a region was abolished at the end of July 2008. 

#This script will download all data up to August 2014, sort and place all files in subdirectories by region symbol. 

import urllib.request
import os
import shutil
import sys

months = ['01_','02_','03_','04_','05_','06_','07_','08_','09_','10_','11_','12_']
states = ['NSW', 'QLD','SA', 'VIC']
ext = "1.csv"
years = ['1999','2000','2001','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2012','2013']
currentyrmonths = ['01_','02_','03_','04_','05_','06_','07_','08_']
curstates = ['NSW', 'QLD','SA', 'VIC','TAS']
allyears = ['1998']+ years + ['2014']

result = []

for state in states:
    result.append(("1998"+"12_"+state+ext))

result.append(("1998"+"12_"+"SNOWY"+ext))

for year in years:
    for month in months:
        for state in states:
            result.append((year+month+state+ext))

for year in years[0:10]:
    for month in months:
        result.append((year+month+"SNOWY"+ext))

for month in months[0:6]:
    result.append(("2008"+month+"SNOWY"+ext))

for year in years[8:17]:
    for month in months:
        result.append((year+month+"TAS"+ext))

for month in months[4:11]:
    result.append(("2005"+month+"TAS"+ext))
        
for month in months[0:8]:
    for curstate in curstates:
        result.append(("2014"+month+curstate+ext))    

print(' Created list of all data files')

for index in range(len(result)):
    URL ="http://www.nemweb.com.au/mms.GRAPHS/data/DATA"+result[index]
    filename = "DATA"+result[index]
    urllib.request.urlretrieve(URL, filename)
    print('.', end='', flush=True)
    
allstates = states + ["SNOWY","TAS"]
for allstate in allstates:
    try:
        os.makedirs("./AEMO/"+allstate)
    except OSError:
   #Directory either already exists or permission denied
        pass
    print('.', end='', flush=True)

for allstate in allstates:
    for allyear in allyears:
        for month in months:
            try:
                shutil.move("./"+"DATA"+allyear+month+allstate+ext,"./AEMO/"+allstate+"/")
            except OSError:
                pass
            print('.', end='', flush=True)
            
print(' Downloading and Sorting Complete')












