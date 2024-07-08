import pandas as pd
import numpy as np
import seaborn as sbn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics

dataset = pd.read_csv("Social_Network_Ads.csv")
#print(dataset.isnull().sum())
print(dataset)
label_encoder = LabelEncoder()
dataset["Gender"] = label_encoder.fit_transform(dataset["Gender"])
x=dataset.iloc[:,1:4]
y=dataset.iloc[:,-1]

train_a,test_a,train_b,test_b = train_test_split(x,y,test_size=0.2)
model = LogisticRegression()
model.fit(train_a.values,train_b.values)
pred = model.predict(test_a.values)
print(metrics.accuracy_score(pred,test_b)*100)
'''
test_x =np.array([[0,19,25000]])
print(model.predict(test_x))
'''
#df = pd.DataFrame(test_a,pred)

print("\nConfusion Matrix :\n",confusion_matrix(test_b,pred))
print("\nClassification Report :\n",classification_report(test_b,pred))
#sbn.regplot(test_a,pred,data=df,logistic=True,ci=None)