# coding: utf-8
from sqlalchemy import create_engine
import pandas as pd
from pandas import io

rootdir = "/scratch/jslab/aws/"
csvfile = rootdir + "transactions.csv"
transcsv = pd.read_csv(csvfile, iterator=True, chunksize = 100000)
engine = create_engine('sqlite:///'+rootdir + 'trans.sqlite')

tablecur = transcsv.next()
tablecur.to_sql('trans', engine)
io.sql.read_sql_query('SELECT * FROM trans WHERE id=86246 AND category=9753',engine)
io.sql.read_sql_query('SELECT * FROM trans WHERE id=86246 AND category=9753',engine).head()
io.sql.read_sql_query('SELECT id,category,date FROM trans WHERE id=86246 AND category=9753',engine).head()
io.sql.read_sql_query('SELECT category, sum(purchasequantity) AS total FROM trans GROUP BY id', engine)
io.sql.read_sql_query('SELECT category, MAX(purchaseamount) AS totalamount FROM trans GROUP BY id', engine)
io.sql.read_sql_query('SELECT id, category,MAX(purchaseamount) AS totalamount  FROM trans GROUP BY id ORDER BY totalamount', engine)
