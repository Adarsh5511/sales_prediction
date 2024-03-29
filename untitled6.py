# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10HHLyBYEMX_ocANQ1lJhXyotkyca2Cgx
"""

import pandas as pd

sales=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Big%20Sales%20Data.csv')

sales.head()

sales.columns

sales['Item_Weight'].fillna(sales.groupby(['Item_Type'])['Item_Weight'].transform('mean'),inplace=True)

sales.info()

sales.describe()

import seaborn as sns

sns.pairplot(sales)

sales[['Item_Identifier']].value_counts()

sales[['Item_Fat_Content']].value_counts()

sales.replace({'Item_Fat_Content':{'LF':'Low Fat','reg':'Regular','low fat':'Low Fat'}}, inplace=True)

sales[['Item_Fat_Content']].value_counts()

sales.replace({'Item_Fat_Content':{'Low Fat': 0,'Regular': 1}}, inplace=True)

sales[['Item_Type']].value_counts()

sales.replace({'Item_Type':{'Fruits and Vegetables': 0,'Snack Foods':0,'Household': 1,
                    'Frozen Foods':0,'Dairy' :0,'Baking Goods':0,'Canned':0,'Health and Hygiene':1,
                      'Meat':0,'Soft Drinks':0,'Breads':0,'Hard Drinks':0 ,'Others':2,'Starchy Foods':0,
                         'Breakfast':0,'Seafood':0   }},inplace=True)

sales[['Item_Type']].value_counts()

sales[['Outlet_Identifier']].value_counts()

sales.replace({'Outlet_Identifier':{'OUT027':0,
'OUT013':1,
'OUT035':4 ,
'OUT046':3  ,
'OUT049':2,
'OUT045':5 ,
'OUT018':6  ,
'OUT017':7 ,
'OUT010':8  ,
'OUT019':9  ,        }},inplace=True)

sales[['Outlet_Identifier']].value_counts()

sales[['Outlet_Size']].value_counts()

sales.replace({'Outlet_Size':{'Medium':1,
'Small':0,
'High':2}},inplace=True)

sales[['Outlet_Size']].value_counts()

sales[['Outlet_Location_Type']].value_counts()

sales.replace({'Outlet_Location_Type':{'Tier 3':2,
'Tier 2':1 ,
'Tier 1' :0 ,                }},inplace=True)

sales[['Outlet_Location_Type']].value_counts()

sales[['Outlet_Type']].value_counts()

sales.replace({'Outlet_Type':{'Supermarket Type1' :1,
'Grocery Store':0,
'Supermarket Type3':3,
'Supermarket Type2':2,}},inplace=True)

sales[['Outlet_Type']].value_counts()

sales.head()

sales.info()

sales.shape

y=sales['Item_Outlet_Sales']

y.shape

y

X=sales.drop(['Item_Identifier','Item_Outlet_Sales'], axis=1)

X.shape

X

from sklearn.preprocessing import StandardScaler

sc= StandardScaler()

X_std=sales[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']]

X_std=sc.fit_transform(x_std)

X_std

X[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']]=pd.DataFrame(X_std,columns=[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']])

X

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=2529)

X_train.shape,X_test.shape,y_train.shape,y_test.shape

from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor(random_state = 2529)

rfr.fit(X_train,y_train)

y_pred=rfr.predict(X_test)

y_pred.shape

y_pred

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mean_squared_error(y_test,y_pred)

mean_absolute_error(y_test,y_pred)

r2_score(y_test,y_pred)

import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred)
plt.xlabel("Actual prices")
plt.ylabel("Predicted prices")
plt.title("Actual prices vs Predicted price")
plt.show()



