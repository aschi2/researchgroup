import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
import numpy as np



data = pd.read_csv('combined.csv',index_col=0)


del data['precipType']
X = data.iloc[:,0:15]
X.replace(np.nan,value = 0,inplace=True)
Y = data.iloc[:,-1:]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)


RF = RandomForestClassifier(n_estimators = 500)
model = RF.fit(X_train,np.array(Y_train).ravel())
Ada = AdaBoostClassifier(n_estimators=500)
model2 = Ada.fit(X_train,np.array(Y_train).ravel())
Grad = GradientBoostingClassifier(n_estimators = 500, learning_rate = 1, max_depth = 1, random_state = 0)
model3 = Grad.fit(X_train,np.array(Y_train).ravel())
cvs = cross_val_score(model,X_test,np.array(Y_test).ravel(),cv = 100)
cvs2 = cross_val_score(model2,X_test,np.array(Y_test).ravel(),cv = 100)
cvs3 = cross_val_score(model3,X_test,np.array(Y_test).ravel(),cv = 100)
mean_cvs = np.mean(np.array(cvs))
mean_cvs2 = np.mean(np.array(cvs2))
mean_cvs3 = np.mean(np.array(cvs3))
print("Random Forest Accuracy: " + str(mean_cvs))
print("Ada Boosted Trees Accuracy: " + str(mean_cvs2))
print("Gradient Boosted Trees Accuracy: " + str(mean_cvs3))