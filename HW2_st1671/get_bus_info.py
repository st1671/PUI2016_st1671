import json
import urllib2 
import os
import sys
import csv

apikey = sys.argv[1]
busn = sys.argv[2]
busncsv = sys.argv[3]


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,busn)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
vehicleact = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity']
busnum = len(vehicleact)

with open(busn,'w') as csvfile:
    fieldnames = ['Latitude', 'Longtitude', 'Stop Name', 'Stop Status']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for i in range(busnum):
        Location = vehicleact[i][u'MonitoredVehicleJourney'][u'VehicleLocation']
        lat = str(Location[u'Latitude'])
        lon = str(Location[u'Longitude'])
        stname = str(vehicleact[i][u'MonitoredVehicleJourney'][u'MonitoredCall'][u'StopPointName'])
        ststat = str(vehicleact[i][u'MonitoredVehicleJourney'][u'OnwardCalls'][u'OnwardCall'][0][u'Extensions'][u'Distances'][u'PresentableDistance'])
        writer.writerow({'Latitude':lat, 'Longtitude':lon, 'Stop Name':stname, 'Stop Status':ststat })

