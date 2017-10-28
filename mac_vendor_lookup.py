#!/usr/bin/python
#
#name: mac_vendor_lookup.py
#date: 10/28/2017
#laguage: python
#
#This script is written to work with the API built into: https://macvendors.com/
#The API url is: http://api.macvendors.com/
#Example get: http://api.macvendors.com/FC:FB:FB:01:FA:21
#
#The requests module is required. Thats not included in standard library.
#
#This script reads a file of mac addresses and then uses request.get to obtain the data from macvendors.com
#
#No guantees
#Use at your own risk.
#

import requests
import sys

list01=[]
var05=sys.argv[1]
var06=open(var05,'r')

for line in var06:
        list01.append(line.strip('\n'))

print"\n"
print"-------------------------------------------"
for line01 in list01:
        var01='http://api.macvendors.com/%s' % (line01)
        r = requests.get(var01)
        print line01 +' : '+r.content
print"-------------------------------------------"
print"\n"
