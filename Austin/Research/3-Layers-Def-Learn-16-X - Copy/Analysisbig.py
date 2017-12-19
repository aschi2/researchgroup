import pandas as pd
import numpy as np
import tflearn as tfl
import random
import sklearn
from sklearn.model_selection import train_test_split
import os
from loss import *
import h5py

#os.chdir("C:\\Users\\Austin Chi\\Dropbox\\Research Project Austin\\researchgroup\\Austin\\Research")


label = str(random.randint(0,100000000))
MODEL_NAME = "Regional_3_layers"
PATH = "C:\\Users\\Austin Chi\\Desktop"

h5 = h5py.File('firedata.h5','r')
X_train = h5['X']
y_train = h5['Y']



#Start Model
test_net = tfl.input_data(shape = [None,21],name = 'input')
test_net = tfl.layers.normalization.batch_normalization(test_net)
                                                                                                               
test_net = tfl.layers.core.fully_connected(test_net,1024,activation='relu',weights_init = 'normal',bias = True,bias_init = 'normal',regularizer = 'L2')
test_net = tfl.layers.core.dropout(test_net,.73)

test_net = tfl.layers.core.fully_connected(test_net,2048,activation='relu',weights_init = 'normal',bias = True,bias_init = 'normal',regularizer = 'L2')
test_net = tfl.layers.core.dropout(test_net,.73)

test_net = tfl.layers.core.fully_connected(test_net,1024,activation='relu',weights_init = 'normal',bias = True,bias_init = 'normal',regularizer = 'L2')
test_net = tfl.layers.core.dropout(test_net,.73)

test_net = tfl.layers.core.fully_connected(test_net,1,activation='softmax',bias = True,name = 'To_Output')
#                                           This learning rate seems to marginally help with local minimums
test_net = tfl.layers.estimator.regression(test_net, name = "output",loss = custom_loss)

model = tfl.DNN(test_net, 
                tensorboard_verbose = 0,
                best_checkpoint_path='C:\\Users\\Austin Chi\\Dropbox\\Research Project Austin\\researchgroup\\Austin\\Research\\3-Layers-Def-Learn-16-X - Copy\\Best'
                )

if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    print("Model Loaded")
else:
    model.fit(X_train, y_train,validation_set = .2,n_epoch = 5000, snapshot_step = 5000, show_metric = True,run_id = MODEL_NAME)
    model.save(PATH + MODEL_NAME)

#Best Accuracy, 74%

