import urllib
import json

#this is to set the new URL that google maps will use
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    #this is to enter the location
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    #use urlencode to pass more parameters to URL
    url = serviceurl + urllib.urlencode({'sensor' : 'false', 'address':address})
    print 'Retrieving', url
    #read URL data here
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'reterived', len(data), 'characters'
    #load to json to deal with the downloaded json data
    try: js = json.loads(str(data))
    except : js = None
    #read the status of the json if it is ok, it successfully retrive the json data
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure to Retrive ===='
        print data
        continue
    #if there is data in this jason, which means the status of its header is ok, then we do some job to parse it
    print json.dumps(js, indent = 4)
    #retervet the information in data that has been pared by the json
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat', lat,'lng',lng
    #this is to pritn the formatted_address, it is really interesting
    location = js['results'][0]['formatted_address']
    print location
