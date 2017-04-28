import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np
import tflearn as tfl

data = pd.read_csv('combined.csv')
del data['precipType']
del data['icon']
X = data.iloc[:,1:12]
X.replace(np.nan,value = 0,inplace=True)
Y = data.iloc[:,-1:]
enc = sklearn.preprocessing.OneHotEncoder(sparse = False)
enc.fit(Y)
Y = enc.transform(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y)

test_net = tfl.input_data(shape = [None,11],name = 'in')
test_net = tfl.layers.normalization.batch_normalization(test_net)
test_net = tfl.layers.core.fully_connected(test_net,1500,activation='relu',bias = True)
test_net = tfl.layers.core.fully_connected(test_net,1000,activation='relu',bias = True)
test_net = tfl.layers.core.fully_connected(test_net,2,activation='relu',bias = True)
test_net = tfl.layers.estimator.regression(test_net, name = "fire")

model = tfl.DNN(test_net)
model.fit(np.array(X_train) , y_train ,validation_set = (np.array(X_test), y_test),n_epoch = 10, snapshot_step = 500, show_metric = True)

# SVM_RBF_Model = SVC(probability= True,decision_function_shape= "ovo")
# LOG_Model = LogisticRegression(n_jobs = -1)

# LOG_Model.fit(X_train,y_train)
# scores_LOG = cross_val_score(LOG_Model, X_test,y_test['fire'], cv = 5)
# np.mean(scores_LOG)

# SVM_RBF_Model.fit(X_train, y_train)
# scores_SVM = cross_val_score(SVM_RBF_Model, X_test, y_test['fire'], cv=5)
# np.mean(scores_SVM)