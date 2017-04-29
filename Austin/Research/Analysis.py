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
#                                                                                                                                   Regularizer helps overfitting
test_net = tfl.layers.core.fully_connected(test_net,2048,activation='relu',weights_init = 'normal',bias = True,bias_init = 'normal',regularizer = 'L2')
#Dropout Layer helps overfitting
test_net = tfl.layers.core.dropout(test_net,.73)
test_net = tfl.layers.core.fully_connected(test_net,1024,activation='relu',weights_init = 'normal',bias = True,bias_init = 'normal',regularizer = 'L2')
test_net = tfl.layers.core.dropout(test_net,.73)
test_net = tfl.layers.core.fully_connected(test_net,2,activation='relu',bias = True)
#                                           This learning rate seems to marginally help with local minimums
test_net = tfl.layers.estimator.regression(test_net, name = "fire",learning_rate = .0009)

# Problems with overfitting at .45ish and local minimum at .56ish, If succesful, should get model with 99% accuracy +- .5%
model = tfl.DNN(test_net)
model.fit(np.array(X_train) , y_train ,validation_set = (np.array(X_test), y_test),n_epoch = 20, snapshot_step = 500, show_metric = True)
#Best Accuracy, 99%+-.5%


# LOG_Model = LogisticRegression(n_jobs = -1)
# LOG_Model.fit(X_train,y_train)
# scores_LOG = cross_val_score(LOG_Model, X_test,y_test['fire'], cv = 5)
# np.mean(scores_LOG)
#Accuracy OK, .95%


# SVM_RBF_Model = SVC(probability= True,decision_function_shape= "ovo")
# SVM_RBF_Model.fit(X_train, y_train)
# scores_SVM = cross_val_score(SVM_RBF_Model, X_test, y_test['fire'], cv=5)
# np.mean(scores_SVM)
#Accuracy very poor .75%