from sqlalchemy import create_engine
import panda as pd
from pandas import io


csvfile = "/Documents/transactions.csv"

transactions_df = pd.read_csv(csvfile, iterator=True, chunksize = 10000)

engine = create_engine('')
