import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score,accuracy_score

df1=pd.read_csv("Inventory_new_data.csv")
# 

from sklearn.preprocessing import OrdinalEncoder,LabelEncoder

oe=OrdinalEncoder(categories=[['Adaptar', 'Battery', 'CORD', 'Cable', 'Carrying Case',
       'Carrying case', 'Controller Card', 'Docking', 'Graphic Card',
       'HDD_NB_DT', 'Keyboard_DT', 'Keyboard_NBK', 'LCD', 'MOUSE',
       'Memory', 'Network Card', 'Nic Card', 'ODD', 'ODD Mechanical',
       'ODM Mechanical', 'Projector', 'SSD_NB_DT', 'Security Lock',
       'Speaker', 'Wireless',"Adapter"]])
le=LabelEncoder()

df1["Product"]=oe.fit_transform(df1[["Product"]])
df1["Demand"]=le.fit_transform(df1[["Demand"]])

# print(df1)

df1["Product"]=df1["Product"].astype(int)


x=df1.iloc[:,:4]
y=df1.iloc[:,4]


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

svc=SVC()
deci=DecisionTreeClassifier()
logi=LogisticRegression()
rand=RandomForestClassifier(n_estimators=10)

base_learner=[("svc",svc),("deci",deci),("logi",logi),("rand",rand)]

voting=VotingClassifier(estimators=base_learner,)

voting.fit(x_train,y_train)

y_pred=voting.predict(x_test)

# print(r2_score(y_test,y_pred))
# print(accuracy_score(y_test,y_pred))



Store_code=[1,2,3,4,5,6,7,8,9,10,11,12,1,14,15]
Store_Location=["Pratap Nagar","Sitapura","Jagatpura","Malviya Nagar","Gandi Nagar","Raja Park","Durgapura","Gopalpura","Maheshnagar","Tonk Phatak","Gurjar ki Thadi","Shyam Nagar","Mansarovar","Nirman Nagar","Vaishali Nagar"]
Store_location_Code=pd.DataFrame(Store_Location,columns=["Store Location"])
Store_location_Code["Code"]=Store_code

# print(Store_location_Code)




product_name=['Battery', 'CORD', 'Cable', 'Carrying Case',
       'Carrying case', 'Controller Card', 'Docking', 'Graphic Card',
       'HDD_NB_DT', 'Keyboard_DT', 'Keyboard_NBK', 'LCD', 'MOUSE',
       'Memory', 'Network Card', 'Nic Card', 'ODD', 'ODD Mechanical',
       'ODM Mechanical', 'Projector', 'SSD_NB_DT', 'Security Lock',
       'Speaker', 'Wireless','Adaptar']
# len(product_name)
product_name=pd.DataFrame(product_name,columns=["Original"])
product_name["Encoded Code"]=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# product_name
# print(product_name)