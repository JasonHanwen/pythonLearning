import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor' : 'false', 'address':address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'reterived', len(data), 'characters'

    try: js = json.loads(str(data))
    except : js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure to Retrive ===='
        print data
        continue
    #if there is data in this jason, which means the status of its header is ok, then we do some job to parse it
    print json.dumps(js, indent = 4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat', lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
