# Australian Energy Market Operator (AEMO) 5 minute Dispatch Demand data script
# Released as open source and developed by Dr Liam Wagner, http://www.liamwagner.com/
# liam dot wagner at gmail dot com
# http://github.com/ldw77/Energy-Data/
# All data downloaded by this script is provided copyright free by AEMO http://www.aemo.com.au

# This script will download all available data (2004 to August 2014), sort and place all files in
# a subdirectory HISTDEMAND. 

import urllib.request
import os
import shutil
import sys

months = ['01','02','03','04','05','06','07','08','09','10','11','12']
ext = "01.ZIP"
years = ['2005','2006','2007','2008','2009','2010','2011','2012','2012','2013']
allyears = ['2004']+ years + ['2014']

result = []

for year in years:
    for month in months:
            result.append(("PUBLIC_HISTDEMAND_"+year+month+ext))

for month in months[6:12]:
    result.append(("PUBLIC_HISTDEMAND_"+"2004"+month+ext))

for month in months[0:7]:
    result.append(("PUBLIC_HISTDEMAND_"+"2014"+month+ext))

#print(result)
print(' Created list of all data files')


for index in range(len(result)):
    URL ="http://www.nemweb.com.au/REPORTS/ARCHIVE/HistDemand/"+result[index]
    filename = result[index]
    urllib.request.urlretrieve(URL, filename)
    print('.', end='', flush=True)

try:
    os.makedirs("./AEMO/HISTDEMAND/")
except OSError:
   #Directory either already exists or permission denied
    pass
print('.', end='', flush=True)


for index in range(len(result)):
    try:
        shutil.move(result[index],"./AEMO/HISTDEMAND/")
    except OSError:
        pass
print('.', end='', flush=True)
