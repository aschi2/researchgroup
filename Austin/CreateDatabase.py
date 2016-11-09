
# coding: utf-8

# ### This will read a CSV file into an SQLITE file

# In[ ]:

from sqlalchemy import create_engine
import pandas as pd
from pandas import io

rootdir = "/scratch/jslab/aws/"
csvfile = rootdir + "firedata.csv"
firecsv = pd.read_csv(csvfile, iterator=True, chunksize = 100)

engine = create_engine('sqlite:///'+rootdir + 'calfire.sqlite')

tablecur = firecsv.next()
tablecur.head()

for tablecur in firecsv:
    tablecur.to_sql('fire',engine,if_exists='append')

