# EIA energy data script
# Released as open source and developed by Liam Wagner, http://www.liamwagner.com/
# liam dot wagner at gmail dot com
# http://github.com/ldw77/Energy-Data/


#This python script uses the bulk download facilities of the Energy Information Agency,
#within the US Department of Energy to acquire all of their API data sets (as at 21st July 2014).
#All data downloaded by this script is provided copyright free.

import urllib.request
import os

try:
    os.makedirs("datasources/EIA_data")
except OSError:
    #Directory either already exists or permission denied
    pass
print('.', end='', flush=True)

# Firstly you may want to download the manifest
URL ="http://api.eia.gov/bulk/manifest.txt"
filename = "datasources/EIA_data/manifest.txt"
urllib.request.urlretrieve(URL, filename)
print(' EIA Manifest Done') 

#Download all files from the EIA, US Department of Energy bulk data facility
####BEWARE these data sets are VERY LARGE (>2Gb for all files)

URL ="http://api.eia.gov/bulk/PET.zip"
filename = "datasources/EIA_data/PET.zip"
urllib.request.urlretrieve(URL, filename)
print(' Petroleum and other liquid fuels Done')

URL ="http://api.eia.gov/bulk/SEDS.zip"
filename = "datasources/EIA_data/SEDS.zip"
urllib.request.urlretrieve(URL, filename)
print(' State Energy Data System Done')

URL ="http://api.eia.gov/bulk/AEO.zip"
filename = "datasources/EIA_data/AEO.zip"
urllib.request.urlretrieve(URL, filename)
print(' Annual Energy Outlook Done')

URL ="http://api.eia.gov/bulk/COAL.zip"
filename = "datasources/EIA_data/COAL.zip"
urllib.request.urlretrieve(URL, filename)
print(' Coal Done')

URL ="http://api.eia.gov/bulk/ELEC.zip"
filename = "datasources/EIA_data/ELEC.zip"
urllib.request.urlretrieve(URL, filename)
print(' Electricity Done')

URL ="http://api.eia.gov/bulk/NG.zip"
filename = "datasources/EIA_data/NG.zip"
urllib.request.urlretrieve(URL, filename)
print(' Natural Gas Done')

URL ="http://api.eia.gov/bulk/STEO.zip"
filename = "datasources/EIA_data/STEO.zip"
urllib.request.urlretrieve(URL, filename)
print(' Short-Term Energy Outlook Done')


print(' All Done')
