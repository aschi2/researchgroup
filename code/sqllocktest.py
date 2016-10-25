from sqlalchemy import create_engine
import pandas as pd
from pandas import io

rootdir = "/scratch/jslab/aws/"
csvfile = rootdir + "transactions.csv"
transcsv = pd.read_csv(csvfile, iterator=True, chunksize = 100000)

engine = create_engine('sqlite:///'+rootdir + 'trans.sqlite')

tablecur = transcsv.next()
tablecur.head()

tablecur.to_sql('trans',engine,if_exists='append')

