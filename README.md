Energy-Data
===========

![](http://www.liamwagner.com/images/Phuket.jpg)


Open Energy Data Project
=======
This project will allow a user to acquire the latest energy data sets that are publicly available. Only publicly available data will be included into the database, however I will be providing links to subscription services that others may find useful.

Download the data
=======
Firstly, we must acquire the data.
* **EIA** API data bank is a rapidly growing database of US and some global energy indicators. This scrapper acquires the data (>2Gb)
  * Energy-Data / download / EIA_BulkDownload.py

* **Australian Energy Market Operator**
 * Half Houly Spot Market Prices and Demand 
   * Energy-Data / download / AEMO_Spot_Demand_Half_Hourly.py
 * Historial 5 Minute Demand files for the last 10 years
   * Energy-Data / download / AEMO_Hist_demand5min.py

* **Economic Data** acquire Federal Reserve 8th District's FRED data bank, the World Bank's Development Indicators and the Maddison Data set on economic development
  * Energy-Data / download / EconomicData_BulkDownload.py
