import urllib2
import shutil
import os
import popen2
import requests
from lxml import html
from bs4 import BeautifulSoup

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, "https://dds.cr.usgs.gov/emodis/CONUS/historical/TERRA/", "woodardjoshua@gmail.com", "USGSwoodard14")
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
opener.open("https://dds.cr.usgs.gov/emodis/CONUS/historical/TERRA/")
urllib2.install_opener(opener)

#TODO: now loop over all year directories for  *.US_eMTH_NDVI.YYYY.DDD-DDD.QKM.COMPRES...zip files
#for example .../TERRA/2014/US_eMTH_NDVI.2014.365-006.QKM.COMPRES.*
res =urllib2.urlopen("https://dds.cr.usgs.gov/emodis/CONUS/historical/TERRA/")
html = res.read()
Soup = BeautifulSoup(html)
tags = Soupww('a')
print tags
