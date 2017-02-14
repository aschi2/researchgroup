import requests
import json
import pandas
from datetime import datetime
from urllib2 import Request, urlopen

def DSTimeMachine(lat, lon, time,api = 'ae81c74d7b434000492e19b44facafc0'):
    """Takes lat (float), lon (float), time (int) and api key (string) (optional), returns an 1 x n pandas dataframe."""
    url = "https://api.darksky.net/forecast/%s/%f,%f,%d"
    query = url % (api,lat,lon,time)
    r = requests.get(query)
    df = pandas.read_json(r.text)
    testerdf = pandas.DataFrame(df['currently'])
    test2 = pandas.DataFrame.transpose(testerdf)
    return test2

def toUnix(d, time):
    """Takes in Date (DateTime Object?) and Time(Int?), returns unix time"""
    time = str(time)
    if (len(time) == 3):
        time = '0' + time
    extra = time[len(time) - 2:len(time)]
    extra = ":" + extra
    time = time[:-2]
    time = time + extra
    date = d.strftime('%Y-%m-%d')
    date = date+" "+time
    datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M')
    return (datetime_object - datetime(1970,1,1)).total_seconds()

def GOElevation(lat,lon,api = "AIzaSyCDrKYZg1yY9uGU078F-vgtw9T2mcmn4-0"):
    """Takes lat (float), lon (float), and api key (string) (optional), returns a float number """
    url = "https://maps.googleapis.com/maps/api/elevation/json?locations=%f,%f&key=%s"
    qurl = url % (lat,lon,api)
    r = requests.get(qurl)
    df = pandas.read_json(r.text)
    dfprime = pandas.DataFrame(df)
    flt = [dfprime["results"][0]['elevation']]
    dfprime2 = pandas.DataFrame(flt,columns=["Elevation"])
    return dfprime2
