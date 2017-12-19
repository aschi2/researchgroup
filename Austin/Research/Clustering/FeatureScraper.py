import requests
import json
import pandas
from datetime import datetime
from urllib2 import Request, urlopen
import numpy as np

def DSTimeMachine(lat, lon, time,api):
    """Takes lat (float), lon (float), time (int) and api key (string) (optional), returns an 1 x n pandas dataframe."""
    url = "https://api.darksky.net/forecast/%s/%f,%f,%d"
    query = url % (api,lat,lon,time)
    r = requests.get(query)
    df = pandas.read_json(r.text)
    try:
        testerdf = pandas.DataFrame(df['currently'])
        test2 = pandas.DataFrame.transpose(testerdf)
        return test2
    except:
        return np.nan

def fromStringtoUnix(d, time):
    """Takes in Date (DateTime Object?) and Time(Int?), returns unix time"""
    time = str(time)
    if (len(time) == 3):
        time = '0' + time
    extra = time[len(time) - 2:len(time)]
    extra = ":" + extra
    time = time[:-2]
    time = time + extra
    d = datetime.strptime(str.split(d)[0],'%m/%d/%Y')
    date = d.strftime('%m/%d/%Y')
    date = date+" "+time
    datetime_object = datetime.strptime(date, '%m/%d/%Y %H:%M')
    return (datetime_object - datetime(1970,1,1)).total_seconds()

def GOElevation(lat,lon,api):
    """Takes lat (float), lon (float), and api key (string) (optional), returns a float number """
    url = "https://maps.googleapis.com/maps/api/elevation/json?locations=%f,%f&key=%s"
    qurl = url % (lat,lon,api)
    r = requests.get(qurl)
    df = pandas.read_json(r.text)
    dfprime = pandas.DataFrame(df)
    try:
        flt = [dfprime["results"][0]['elevation']]
        dfprime2 = pandas.DataFrame(flt,columns=["Elevation"])
        return dfprime2
    except:
        return np.nan

def ReverseGeoZip(lat, lon, api):
    """Takes lat (float), lon (float), and api key (string) (optional), returns zipcode for now, plan to return distance to nearest city in the future"""
    sensor = 'false'
    base = "https://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}&result_type=postal_code&key={api}".format(
        lat=lat,
        lon=lon,
        sen=sensor,
        api=api
    )
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    x = json.loads(response.text)
    try:
        zipcode = x['results'][0]['address_components'][0]['short_name']
        return zipcode
    except:
        return np.nan


def ReverseGeoState(lat, lon, api, short = True):
    """Takes lat (float), lon (float), and api key (string) (optional), returns State, short bool will return short name if true, long name if false"""
    sensor = 'false'
    base = "https://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}&result_type=postal_code&key={api}".format(
        lat=lat,
        lon=lon,
        sen=sensor,
        api=api
    )
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    x = json.loads(response.text)
    if short == False:
        try:
            longname = x['results'][0]['address_components'][3]['long_name']
            return longname
        except:
            return np.nan
    try:
        shortname = x['results'][0]['address_components'][3]['short_name']
        return shortname
    except:
        return np.nan