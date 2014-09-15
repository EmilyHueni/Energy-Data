# Australian Energy Market Operator (AEMO) Public Dispatch data download script 
# Released as open source and developed by Dr Liam Wagner, http://www.liamwagner.com/
# liam dot wagner at gmail dot com
# http://github.com/ldw77/Energy-Data/
# All data downloaded by this script is provided copyright free by AEMO http://www.aemo.com.au

# This script will download all available data for the Last 90 Days, sort and place all files in
# a subdirectory DISPATCH. 


import urllib.request
import os
import shutil
import sys
import datetime

result=[]

start = datetime.datetime.strptime("16-08-2013", "%d-%m-%Y")
end = datetime.datetime.strptime("14-09-2014", "%d-%m-%Y")
date_generated = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))

for date in date_generated:
    result.append(date.strftime("%Y%m%d")+".ZIP")

for index in range(len(result)):
    URL ="http://www.nemweb.com.au/REPORTS/ARCHIVE/Dispatch_Reports/PUBLIC_DISPATCH_"+result[index]
    filename = "PUBLIC_DISPATCH_"+result[index]
    urllib.request.urlretrieve(URL, filename)
    print('.', end='', flush=True)

try:
    os.makedirs("./AEMO/Dispatch/")
except OSError:
   #Directory either already exists or permission denied
    pass
print('.', end='', flush=True)

for index in range(len(result)):
    try:
        shutil.move("PUBLIC_DISPATCH_"+result[index],"./AEMO/Dispatch/")
    except OSError:
        pass
print('.', end='', flush=True)

print(result)
