import urllib
import json

location = "서신동"
data = urllib.urlopen("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=" + location)
json = json.loads(data.read())

latitude = json["results"][0]["geometry"]["location"]["lat"]
longitude = json["results"][0]["geometry"]["location"]["lng"]

