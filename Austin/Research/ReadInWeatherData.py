import requests
import json
import pandas

def DSTimeMachine(lat, lon, time,api = 'ae81c74d7b434000492e19b44facafc0'):
    """Takes lat (float), lon (float), time (int) and api (string) (optional), returns an 1 x n pandas dataframe."""
    url = "https://api.darksky.net/forecast/%s/%f,%f,%d"
    query = url % (api,lat,lon,time)
    r = requests.get(query)
    df = pandas.read_json(r.text)
    testerdf = pandas.DataFrame(df['currently'])
    test2 = pandas.DataFrame.transpose(testerdf)
    return test2

