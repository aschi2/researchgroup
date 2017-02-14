import requests
import json
import pandas

def DSTimeMachine(lat, lon, time,api = 'ae81c74d7b434000492e19b44facafc0'):
    """Takes lat (float), lon (float), time (int) and api key (string) (optional), returns an 1 x n pandas dataframe."""
    url = "https://api.darksky.net/forecast/%s/%f,%f,%d"
    query = url % (api,lat,lon,time)
    r = requests.get(query)
    df = pandas.read_json(r.text)
    testerdf = pandas.DataFrame(df['currently'])
    test2 = pandas.DataFrame.transpose(testerdf)
    return test2



def ElAPI(lat,lon,api = "AIzaSyCDrKYZg1yY9uGU078F-vgtw9T2mcmn4-0"):
    """Takes lat (float), lon (float), and api key (string) (optional), returns a float number """
    url = "https://maps.googleapis.com/maps/api/elevation/json?locations=%f,%f&key=%s"
    qurl = url % (lat,lon,api)
    r = requests.get(qurl)
    df = pandas.read_json(r.text)
    dfprime = pandas.DataFrame(df)
    flt = dfprime["results"][0]['elevation']
    dfprime2 = pandas.DataFrame(flt,columns=["Elevation"])
    return dfprime2



    