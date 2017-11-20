
'''program to find  upcoming buses and their locations. Enter the API key and line number'''

import sys
import urllib2
import json

if len(sys.argv) < 3:
	exit(0)
'''if the number of inputs is not correct, exit'''
apiKey= sys.argv[1]
lineInput = sys.argv[2]
address= "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=" + apiKey + "&version=2&LineRef=" +lineInput + "&VehicleMonitoringDetailLevel=call"
response= urllib2.urlopen(address).read()

resStr= response.decode('utf-8')
resJSON= json.loads(resStr)

x = 0
t = resJSON["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

print("Bus Line : " + lineInput)
print("Number of Active Buses : " + str(len(t)))

for e in t:
	loc=e["MonitoredVehicleJourney"]["VehicleLocation"]
	line= "Bus " + str(x) + " is at latitude " + str(loc["Latitude"]) + " and longitude " + str(loc["Longitude"])

	print(line)
	x+=1

'''got help from friend'''
