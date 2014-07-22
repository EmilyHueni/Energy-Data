# Economic databank script
# Released as open source and developed by Liam Wagner, http://www.liamwagner.com/
# liam dot wagner at gmail dot com
# http://github.com/ldw77/Energy-Data/


#This python script uses the bulk download facilities of a range of sources to
#acquire large economic data sets (as at 22nd July 2014).
#All data downloaded by this script is provided copyright free.

import urllib.request
import os

try:
    os.makedirs("datasources/Economics")
except OSError:
    #Directory either already exists or permission denied
    pass
print('.', end='', flush=True)

try:
   os.makedirs("datasources/Economics/FRED")
except OSError:
    #Directory either already exists or permission denied
    pass
print('.', end='', flush=True)

try:
    os.makedirs("datasources/Economics/World_Bank")
except OSError:
    #Directory either already exists or permission denied
    pass
print('.', end='', flush=True)

try:
    os.makedirs("datasources/Economics/Other")
except OSError:
    #Directory either already exists or permission denied
    pass
print('.', end='', flush=True) 

####BEWARE these data sets are realtively LARGE

#Download all files from the Federal Reserve Eighth Division, in St. Louis
#(St. Louis Fed's Economic Research Division, FRED)
#You can download the data as either xls,txt or csv.
URL ="https://research.stlouisfed.org/fred2/downloaddata/FRED2_csv_2.zip"
filename = "datasources/Economics/FRED/FRED2_csv_2.zip"
urllib.request.urlretrieve(URL, filename)
print(' FRED Done')

#World Development Indicators, World Bank
URL ="http://databank.worldbank.org/data/download/WDI_csv.zip"
filename = "datasources/Economics/World_Bank/WDI_csv.zip"
urllib.request.urlretrieve(URL, filename)
print(' WDI Done')

#Maddison Data set on world economic growth
URL ="http://www.ggdc.net/maddison/maddison-project/data/mpd_2013-01.xlsx"
filename = "datasources/Economics/Other/mpd_2013-01.xlsx"
urllib.request.urlretrieve(URL, filename)
print(' Maddison Done')

print(' All Done')
