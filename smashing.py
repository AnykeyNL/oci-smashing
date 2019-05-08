from urllib import request, parse
import json

authtoken = "jhalkfdsjjhsajkdfhskjdhfsakljhfsjhalskjfhderewre"
url = "http://www.oci-workshop.com:3030"

def UpdateMeter(widget, value):
    data = {"auth_token": authtoken, "value": value}
    data = json.dumps(data)
    data = str(data)
    data = data.encode('utf-8')
    req =  request.Request("{}/widgets/{}".format(url, widget), data=data)
    response = request.urlopen(req)
    print ("{} - {}".format(widget, value))

