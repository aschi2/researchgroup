from sqlalchemy import create_engine
import pandas as pd
from pandas import io

rootdir = "/scratch/jslab/aws/"
csvfile = rootdir + "firedata.csv"
transcsv = pd.read_csv(csvfile, iterator=True, chunksize = 100000)

engine = create_engine('sqlite:///'+rootdir + 'calfire.sqlite')

tablecur = transcsv.next()
tablecur.head()

for tablecur in transcsv:
    tablecur.to_sql('fire',engine,if_exists='append')