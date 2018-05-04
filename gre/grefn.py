


from sklearn import model_selection
import pickle
import pandas as pd
import numpy as np
from maintainer import views

def predict(inp):
    #test_verify = pd.read_csv('gender_submission.csv')
    #y_test = test_verify.iloc[:,[1]].values
    #filename = 'titanic_randomForest.sav
    #X_test = np.array((892),(3),(34.5),(0),(0),(7.83),(0),(1),(0),(1),(0))
    #X_test = np.array([[892,3,34.5,0,0,7.83,0,1,0,1,0]])
    X_test = [inp]
    loaded_model = pickle.load(open('gre/gre_randomForest.sav','rb'))
    y_pred = loaded_model.predict(X_test)

    result = str(y_pred)
    if y_pred>0.85:
        s1 = "There is a great chance for you to get the seat. So be prepare for the Interview along with that maintain all the documents proper\n Your score is\n"+"\n"+result+"\n"+"BEST OF LUCK"
        return s1
    else:
        s2 = "There are not huge chances for you it's always a better Idea for you to keep safe opt for the middle level Universities\n"+"-\n"+result+"-\n"+"BEST OF LUCK"
        return s2
