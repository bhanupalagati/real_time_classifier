"""
created on Sun Mar  4 17:40:55 2018

@author: bhanupalagati
"""

# we are using pickle to predict data
from sklearn import model_selection
import pickle
import pandas as pd
import numpy as np
from maintainer import views
import os

def prediction(li):
    #test_verify = pd.read_csv('gender_submission.csv')
    #y_test = test_verify.iloc[:,[1]].values
    #filename = 'titanic_randomForest.sav
    #X_test = np.array((892),(3),(34.5),(0),(0),(7.83),(0),(1),(0),(1),(0))
    #X_test = np.array([[892,3,34.5,0,0,7.83,0,1,0,1,0]])
    X_test = [li]

    loaded_model = pickle.load(open('maintainer/titanic_randomForest.sav','rb'))
    y_pred = loaded_model.predict(X_test)
    if y_pred==1:
        s1 = "That was awesome there are high chances that the person may crossed the TITANIC ship \n This was a pure prediction based on the machine learning strategies\n we are not responsible for any complaints"
        return s1
    else:
        s2 = "We are sorry to reveal that as per the previous AVAILABLE Records and applying lots of machine learning strategies we found that\n Most Probably the person won't be still alive"
        return s2
