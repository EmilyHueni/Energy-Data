# Australian Energy Market Operator (AEMO) Public Daily data download script 
# Released as open source and developed by Dr Liam Wagner, http://www.liamwagner.com/
# liam dot wagner at gmail dot com
# http://github.com/ldw77/Energy-Data/
# All data downloaded by this script is provided copyright free by AEMO http://www.aemo.com.au

# This script will download all available data for the Last 12 Months, sort and place all files in
# a subdirectory Public_Daily. 


import urllib.request
import os
import shutil
import sys
import datetime

result=[]

start = datetime.datetime.strptime("1-1-2012", "%d-%m-%Y")
end = datetime.datetime.strptime("29-08-2014", "%d-%m-%Y")
date_generated = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))

for date in date_generated:
    result.append(date.strftime("%Y%m%d")+".ZIP")

for index in range(len(result)):
    try:
        URL ="http://www.nemweb.com.au/REPORTS/ARCHIVE/Daily_Reports/PUBLIC_DAILY_"+result[index]
        filename = "PUBLIC_DAILY_"+result[index]
        urllib.request.urlretrieve(URL, filename)
        print('.', end='', flush=True)
    except urllib.error.URLError:
        pass

try:
    os.makedirs("./AEMO/Public_Daily/")
except OSError:
   #Directory either already exists or permission denied
    pass
print('.', end='', flush=True)

for index in range(len(result)):
    try:
        shutil.move("PUBLIC_DAILY_"+result[index],"./AEMO/Public_Daily/")
    except OSError:
        pass
print('.', end='', flush=True)

print(result)
