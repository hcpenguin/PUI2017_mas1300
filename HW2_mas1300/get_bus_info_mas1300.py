
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
outputFile=open(lineInput + ".csv", "w+")

resStr= response.decode('utf-8')

resJSON= json.loads(resStr)

x = 0
t = resJSON["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

#print("Bus Line : " + lineInput)
#print("Number of Active Buses : " + str(len(t)))

final= "Latitude,Longitude,Stop Name,Stop Status"
for e in t:
	final+="\r\n"
	m = e["MonitoredVehicleJourney"]
	loc = m["VehicleLocation"]
	lat = loc["Latitude"]
	lon = loc["Longitude"]
	relative =m["MonitoredCall"]
	station = relative["StopPointName"]
	sta = ""
	if len(station) == 0:
		station= "N/A"
	elif station[0] == "":
		station = "N/A"
	else:
		sta = station[0]
	distance = relative["ArrivalProximityText"]
	if distance == "":
		distance = "N/A"
	final += "%f,%f,%s,%s" % (lat, lon, sta, distance)

outputFile.write(final)
outputFile.close()

'''got help from friend not in cusp'''

