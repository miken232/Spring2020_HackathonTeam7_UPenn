#!/usr/bin/env python
# coding: utf-8

# In[1825]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet

from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

from scipy import stats
from scipy.stats import skew


# In[1826]:


df = pd.read_csv('nyc-rolling-sales.csv')
df.head(10)


# In[1827]:


#Dropping useless columns
del df['Unnamed: 0']
df.pivot_table(index='BUILDING CLASS CATEGORY', values='SALE PRICE', aggfunc=np.max)


# In[1828]:


df = df[~df['BUILDING CLASS CATEGORY'].str.contains("BUILDINGS")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("DWELLINGS")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("FACILITIES")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("OTHER")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("HOTELS")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("/")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("LAND")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("COMMERCIAL")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("LOTS")]
df.pivot_table(index='BUILDING CLASS CATEGORY', values='SALE PRICE', aggfunc=np.max)


# In[1829]:


df = df[~df['BUILDING CLASS CATEGORY'].str.contains("18")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("27")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("30")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("34")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("38")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("44")]
df = df[~df['BUILDING CLASS CATEGORY'].str.contains("47")]
df.pivot_table(index='BUILDING CLASS CATEGORY', values='SALE PRICE', aggfunc=np.max)


# In[1830]:


#Check duplicates
sum(df.duplicated(df.columns))


# In[1831]:


#Remove duplicates
df = df.drop_duplicates(df.columns, keep='first')


# In[1832]:


#info
df.info()


# In[1833]:


#Clean
df['LAND SQUARE FEET'] = pd.to_numeric(df['LAND SQUARE FEET'], errors='coerce')
df['GROSS SQUARE FEET']= pd.to_numeric(df['GROSS SQUARE FEET'], errors='coerce')
df['SALE DATE'] = pd.to_datetime(df['SALE DATE'], errors='coerce')
df['SALE MONTH'] = pd.DatetimeIndex(df['SALE DATE']).month
df['SALE PRICE'] = pd.to_numeric(df['SALE PRICE'], errors='coerce')
df['BOROUGH'] = df['BOROUGH'].astype('category')
df['SALE MONTH'] = df['SALE MONTH'].astype('category')
df['ZIP CODE'] = df['ZIP CODE'].astype('category')
df['TAX CLASS AT TIME OF SALE'] = df['TAX CLASS AT TIME OF SALE'].astype('category')


# In[1834]:


#check missing values
df.columns[df.isnull().any()]


# In[1835]:


miss=df.isnull().sum()/len(df)
miss=miss[miss>0]
miss.sort_values(inplace=True)
miss


# In[1836]:


df['LAND SQUARE FEET']=df['LAND SQUARE FEET'].fillna(df['LAND SQUARE FEET'].mean())
df['GROSS SQUARE FEET']=df['GROSS SQUARE FEET'].fillna(df['GROSS SQUARE FEET'].mean())
data=df[~df['SALE PRICE'].isna()]


# In[1837]:


#correlation between the features
corr = data.corr()
#sns.heatmap(corr)


# In[1838]:


#numeric correlation
corr = data.corr()
corr['SALE PRICE'].sort_values(ascending=False)


# In[1839]:


#del data['LAND SQUARE FEET']
numeric_data=data.select_dtypes(include=[np.number])
numeric_data.describe()


# In[1840]:


data=data[data['RESIDENTIAL UNITS']>0]
data['YEAR BUILT'][data['YEAR BUILT']==0]=1800
del data['BLOCK']
del data['LOT']
numeric_data=data.select_dtypes(include=[np.number])
numeric_data.describe()


# In[1841]:


del data['TOTAL UNITS']
del data['COMMERCIAL UNITS']
del data['LAND SQUARE FEET']
numeric_data=data.select_dtypes(include=[np.number])
numeric_data.describe()


# In[1842]:


plt.figure(figsize=(15,6))

sns.boxplot(x='SALE PRICE', data=data)
plt.ticklabel_format(style='plain', axis='x')
plt.title('Boxplot of SALE PRICE in USD')
#plt.show()


# In[1843]:


sns.distplot(data['SALE PRICE'])


# In[1844]:


# Remove observations that fall outside those caps
data = data[(data['SALE PRICE'] > 100000) & (data['SALE PRICE'] < 9000000)]


# In[1845]:


sns.distplot(data['SALE PRICE'])


# In[1846]:


data['SALE PRICE'].skew()


# In[1847]:


sales=np.log(data['SALE PRICE'])
print(sales.skew())
sns.distplot(sales)


# In[1848]:


plt.figure(figsize=(10,6))
sns.boxplot(x='GROSS SQUARE FEET', data=data,showfliers=False)


# In[1849]:


data = data[data['GROSS SQUARE FEET'] < 15000]
plt.figure(figsize=(10,6))
sns.regplot(x='GROSS SQUARE FEET', y='SALE PRICE', data=data, fit_reg=False, scatter_kws={'alpha':0.3})


# In[1850]:


sns.distplot(data['YEAR BUILT'])


# In[1851]:


cat_data=data.select_dtypes(exclude=[np.number])
cat_data.describe()


# In[1852]:


pivot=data.pivot_table(index='NEIGHBORHOOD', values='SALE PRICE', aggfunc=np.median)
pivot


# In[1853]:


# BUILDING CLASS CATEGORY
print(data['BUILDING CLASS CATEGORY'].nunique())

pivot=data.pivot_table(index='BUILDING CLASS CATEGORY', values='SALE PRICE', aggfunc=np.median)
pivot


# In[1854]:


pivot.plot(kind='bar', color='Green')


# In[1855]:


del data['ADDRESS']
del data['APARTMENT NUMBER']


# In[1856]:


data.info()


# In[1857]:


numeric_data=data.select_dtypes(include=[np.number])
numeric_data.columns


# In[1858]:


#transform the numeric features using log(x + 1)
skewed = data[numeric_data.columns].apply(lambda x: skew(x.dropna().astype(float)))
skewed = skewed[skewed > 0.75]
skewed = skewed.index
data[skewed] = np.log1p(data[skewed])


# In[1859]:



# scaler = StandardScaler()
# scaler.fit(data[numeric_data.columns])
# scaled = scaler.transform(data[numeric_data.columns])
#
# for i, col in enumerate(numeric_data.columns):
#        data[col] = scaled[:,i]


# In[1860]:


data.head()


# In[1861]:


del data['BOROUGH']
del data['TAX CLASS AT PRESENT']
del data['EASE-MENT']
del data['BUILDING CLASS AT PRESENT']
del data['ZIP CODE']
del data['TAX CLASS AT TIME OF SALE']
del data['BUILDING CLASS AT TIME OF SALE']
del data['SALE DATE']


# In[1862]:


#Select the variables to be one-hot encoded
one_hot_features = ['BUILDING CLASS CATEGORY','NEIGHBORHOOD','SALE MONTH']


# In[1863]:


# Convert categorical variables into dummy/indicator variables (i.e. one-hot encoding).
one_hot_encoded = pd.get_dummies(data[one_hot_features])
one_hot_encoded.info(verbose=True, memory_usage=True, null_counts=True)


# In[1864]:


# Replacing categorical columns with dummies
fdf = data.drop(one_hot_features,axis=1)
fdf = pd.concat([fdf, one_hot_encoded] ,axis=1)


# In[1865]:


fdf.info()


# In[1866]:


Y_fdf = fdf['SALE PRICE']
X_fdf = fdf.drop('SALE PRICE', axis=1)

X_fdf.shape , Y_fdf.shape


# In[1867]:


X_train ,X_test, Y_train , Y_test = train_test_split(X_fdf , Y_fdf , test_size = 0.3 , random_state =34)


# In[1868]:


# Training set
X_train.shape , Y_train.shape


# In[1869]:


#Testing set
X_test.shape , Y_test.shape


# In[1870]:


# RMSE
def rmse(y_test,y_pred):
      return np.sqrt(mean_squared_error(y_test,y_pred))


# In[1871]:


linreg = LinearRegression(normalize=True)
linreg.fit(X_train, Y_train)
Y_pred_lin = linreg.predict(X_test)


# caculate MSE, MAE, MAPE, and Accuracy
errors = abs(Y_pred_lin - Y_test)
mae = round(np.mean(errors), 2)
mape = round(np.mean(100 * (errors / Y_test)), 2)
accuracy = 100 - mape
print('R-squared: ', round(r2_score(Y_test, Y_pred_lin), 2))
print('RMSE: ', rmse(Y_test,Y_pred_lin))


# In[1872]:


alpha=0.00099
lasso_regr=Lasso(alpha=alpha,max_iter=50000)
lasso_regr.fit(X_train, Y_train)
Y_pred_lasso=lasso_regr.predict(X_test)

errors = abs(Y_pred_lasso - Y_test)
mae = round(np.mean(errors), 2)
mape = round(np.mean(100 * (errors / Y_test)), 2)
accuracy = 100 - mape
print('R-squared: ', round(r2_score(Y_test, Y_pred_lasso), 2))
print('RMSE: ', rmse(Y_test,Y_pred_lasso))


# In[1873]:


rf_regr = RandomForestRegressor()
rf_regr.fit(X_train, Y_train)
Y_pred_rf = rf_regr.predict(X_test)


errors = abs(Y_pred_rf - Y_test)
mae = round(np.mean(errors), 2)
mape = round(np.mean(100 * (errors / Y_test)), 2)
accuracy = 100 - mape
print('R-squared: ', round(r2_score(Y_test, Y_pred_rf), 2))
print('RMSE: ', rmse(Y_test,Y_pred_rf))


# **We can see that Random Forest Regressor has highest R-squared and least RSME score

# In[1874]:


X_test


# In[1875]:


rf_regr.predict(X_test)