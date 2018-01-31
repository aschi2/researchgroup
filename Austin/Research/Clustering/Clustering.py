import pandas
import numpy
from FeatureScraper import *
from sklearn.neighbors import BallTree,radius_neighbors_graph
from networkx import Graph,connected_components
import networkx as nx
import pickle

#Add time to data
data = pandas.read_csv('fires.csv')
def addTime(data):
    """Make sure dataframe has DATE in string and TIME in labeled as GMT"""
    times = list()
    for i in xrange(len(data['DATE'])):
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
    for i in xrange(len(x)):
        sx.append((x[i] - mu)/sd)
    return sx


time = standardize(df.UNIX)
lat = standardize(df.LAT)
long = standardize(df.LONG)
matrix = numpy.asarray((time,lat,long)).T
tree = BallTree(matrix)
sparse = radius_neighbors_graph(tree, .1)
gr = Graph(sparse)
cc = connected_components(gr)
con_list = list(cc)

# create membership vector
n = len(data)
membership = np.zeros(n)
for i, comp in enumerate(cc):
    membership[list(comp)] = i

def ret_group(num,list):
    for i in xrange(len(list)):
        for j in list[i]:
            if j == num:
                return i
                
cluster_list = list()
for i in xrange(len(data)):
    cluster_list.append(ret_group(i,con_list))

df['clusternum'] = cluster_list

pickle.dump(df,open("clusterdataframe.p",'wb'))

pickle.dump(cluster_list,open("cluster_list.p",'wb'))

pickle.dump(cc,open("graphgenerator.p",'wb'))
