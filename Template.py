import numpy as np

import pandas as pd 
 

from sklearn.metrics  import f1_score,accuracy_score

from sklearn.tree import DecisionTreeClassifier
 
# For splitting of data into train and test set
from sklearn.model_selection import train_test_split
train=pd.read_csv("/input/hcirs-ctf/train.csv")
y = train.Class
train.drop(['Class'], axis=1, inplace=True)
X = train
 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2)
DT= DecisionTreeClassifier()
DT.fit(X_train,y_train)
pred=DT.predict(X_test)
 

print(accuracy_score(y_test,pred))
print(f1_score(y_test,pred))

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
print(mean_absolute_error(y_test,pred))
print(mean_absolute_error(y_test,pred))

from sklearn.linear_model import LogisticRegression

from sklearn.svm import SVC

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

from sklearn.linear_model import SGDClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import GradientBoostingClassifier

from lightgbm import LGBMClassifier

from xgboost.sklearn import XGBClassifier

from sklearn.linear_model import LinearRegression

from sklearn.svm import SVR

