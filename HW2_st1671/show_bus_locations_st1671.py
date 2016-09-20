import json
import urllib2 
import os
import sys


apikey = sys.argv[1]
busn = sys.argv[2]


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,busn)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
vehicleact = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity']
busnum = len(vehicleact)
print "Bus Line : ",busn
print "Number of Active Buses :",busnum
for i in range(busnum):
    Location = vehicleact[i][u'MonitoredVehicleJourney'][u'VehicleLocation']
    print "Bus %d is at latitude %f and longitude %f"%(i,Location[u'Latitude'],Location[u'Longitude'])
