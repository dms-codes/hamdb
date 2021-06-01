import requests

urlbase = "http://api.hamdb.org/v1/{}/json/hamdb"

def GetData(callsign):
    url = urlbase.format(callsign)
    res = requests.get(url=url)
    data = res.json()
    return data['hamdb']['callsign']

def GetClass(callsign):
    data = GetData(callsign)
    return data['class']

def GetGrid(callsign):
    data = GetData(callsign)
    return data['grid']

def GetLatLong(callsign):
    data = GetData(callsign)
    return data['lat'], data['long']

def GetName(callsign):
    data = GetData(callsign)
    return data['name']

def GetFullAdress(callsign):
    data = GetData(callsign)
    return data['addr1'], data['addr2'], data['state'], data['zip'], data['country'],    


"""
{
"hamdb": {
"version": "1",
"callsign": {
"call": "VK3YE",
"class": "Advanced",
"expires": "2021-11-23",
"status": "",
"grid": "QF21nw",
"lat": "-38.0504426",
"lon": "145.1208343",
"fname": "",
"mi": "",
"name": "P Parker",
"suffix": "",
"addr1": "5/51 Blantyre Avenue",
"addr2": "CHELSEA",
"state": "VIC",
"zip": "3196",
"country": "Australia"
},
"messages": {
"status": "OK"
}
}
}
"""

if __name__ == "__main__":
    name = GetName("vk3ye")
    print(name)
