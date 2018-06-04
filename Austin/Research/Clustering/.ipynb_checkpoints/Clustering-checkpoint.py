import pandas
import numpy
from FeatureScraper import *
from sklearn.neighbors import BallTree,radius_neighbors_graph
from networkx import Graph,connected_components
import networkx as nx
import pickle
import sqlite3

#Add time to data
print("ok!")
data = pandas.read_csv('fires.csv')
def addTime(data):
    """Make sure dataframe has DATE in string and TIME in labeled as GMT"""
    times = list()
    for i in range(len(data['DATE'])):
        uni = fromStringtoUnix(data['DATE'][i],data['GMT'][i])
        times.append(uni)
    data2 = data
    data2['UNIX'] = times
    return(data2)

df = addTime(data)

matrix = numpy.asarray(data[['LAT','LONG','UNIX']])

def standardize(x):
    mu = np.mean(x)
    sd = np.std(x)
    sx = list()
    for i in range(len(x)):
        sx.append((x[i] - mu)/sd)
    return sx

def dendro(balltree):
    groupnum = list()
    i = .00001
    while(i<.01):
        sparse = radius_neighbors_graph(tree, i,n_jobs=-1)
        gr = Graph(sparse)
        cc = connected_components(gr)
        con_list = list(cc)
        groupnum.append(len(con_list))
        i = i+.00001
    return(groupnum)


time = standardize(df.UNIX)
lat = standardize(df.LAT)
long = standardize(df.LONG)
matrix = numpy.asarray((time,lat,long)).T
tree = BallTree(matrix)
groupnum = list()
sparse = radius_neighbors_graph(tree, .05,n_jobs=-1)
gr = Graph(sparse)
cc = connected_components(gr)
con_list = list(cc)
groupnum.append(len(con_list))

#dendrograph = dendro(tree)
#print(dendrograph)

def ret_group(num,list):
    for i in range(len(list)):
        for j in list[i]:
            if j == num:
                return i
                
cluster_list = list()
for i in range(len(data)):
     cluster_list.append(ret_group(i,con_list))

df['clusternum'] = cluster_list

df['is_duplicated'] = df.duplicated(['clusternum'])

conn = sqlite3.connect("clstr.db")
df.to_sql("data",conn, if_exists="replace")
truedf = df[~df.is_duplicated]
df.to_sql("truedata",conn, if_exists="replace")
# pickle.dump(df,open("clusterdataframe.p",'wb'))

# pickle.dump(cluster_list,open("cluster_list.p",'wb'))

# pickle.dump(cc,open("graphgenerator.p",'wb'))
