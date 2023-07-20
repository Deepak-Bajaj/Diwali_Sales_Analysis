#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing Python Librarires

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


df = pd.read_csv('Diwali Sales Data.csv', encoding = 'unicode_escape')


# In[4]:


df.shape


# In[5]:


df.head


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis = 1, inplace = True)


# In[9]:


#check for null values
pd.isnull(df).sum()


# In[11]:


# drop null values
df.dropna(inplace = True)


# In[13]:


#Change data type
df['Amount'] = df['Amount'].astype('int')


# In[14]:


df['Amount'].dtypes


# In[15]:


df.columns


# In[16]:


# Rename Column
df.rename(columns={'Marital_Status': 'Shaadi'})


# In[17]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc#
df.describe()


# In[5]:


#describe for specific column
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# ## Gender

# In[19]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# ##### Conclusion: from the above graph we can see that most of the buyers are female and even the purchasing power of female is greater then that of men.

# ## Age

# In[13]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group', y= 'Amount', data = sales_age)


# ##### Conclusion: Men and Female both in the age group from 26-35 purchases more also among these female purchase is 3x more then men

# ## State

# In[23]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[44]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(16,7)})
sns.barplot(data = sales_state, x = 'State', y= 'Amount')


# ##### Conclusion: From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# ## Martial Status

# In[24]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc = {'figure.figsize':(7,5)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[29]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount', ascending = False)
sns.set(rc = {'figure.figsize':(10,5)})
sns.barplot(data = sales_state, x = 'Marital_Status', y = 'Amount', hue = 'Gender')


# ##### Conclusion from the above graph we can see that most of the buyers are married women having high purchasing power

# ## Occupation

# In[40]:


ax = sns.countplot(data = df, x = 'Occupation')
sns.set(rc={'figure.figsize':(20, 10)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[45]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(16,7)})
sns.barplot(data = sales_state, x = 'Occupation', y= 'Amount')


# ##### From the above graph analysis we can see that most of the buyers are from IT Sector, Healtcare and Aviation Sector

# ## Product Category

# In[21]:


sns.set(rc={'figure.figsize':(20,15)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


sales_state = df.groupby(['Product_Category'], as_index = False)['Amount'].sum().sort_values(by='Amount', ascending = False).head(10)
sns.set(rc={'figure.figsize':(20, 5)})

sns.barplot(data = sales_state, x = 'Product_Category', y = 'Amount')


# ##### Conclusion: Hence from the above analysis we can see that most of the purchased items are Food, Clothing and Appreal and Electronics gadget

# In[26]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[27]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# In[36]:


product_orders = df.groupby('Product_ID')['Orders'].sum()

# Get the top 10 products with the highest orders
top_10_products = product_orders.nlargest(10)

# Sort in descending order and plot as a bar graph
top_10_products.sort_values(ascending=False).plot(kind='bar')

# Get the user IDs for the top 10 products
top_10_user_ids = df[df['Product_ID'].isin(top_10_products.index)]['User_ID'].unique()

# Print the user IDs
print("User IDs for the top 10 products:")
print(top_10_user_ids)

plt.xlabel('Product ID')
plt.ylabel('Orders')
plt.title('Top 10 Products by Orders')
plt.show()


# In[ ]:


# Got Product ID's for top 10 products aold from particular shop


# In[40]:


product_orders = df.groupby('Product_ID')['Orders'].sum()

# Get the top 10 products with the highest orders
top_1_products = product_orders.nlargest(1)

# Sort in descending order and plot as a bar graph
top_1_products.sort_values(ascending=False).plot(kind='bar')

# Get the user IDs for the top 10 products
top_1_user_ids = df[df['Product_ID'].isin(top_10_products.index)]['User_ID'].unique()

# Create a dictionary to store user fields
user_fields = {}

# Iterate over the top 10 user IDs
for user_id in top_1_user_ids:
    field = df[df['User_ID'] == user_id]['Occupation'].iloc[0]  # Assuming each user has only one field
    if field in user_fields:
        user_fields[field].append(user_id)
    else:
        user_fields[field] = [user_id]

# Print the user fields and their corresponding users
print("User fields:")
for field, users in user_fields.items():
    print(field + ":")
    print(users)

plt.xlabel('Product ID')
plt.ylabel('Orders')
plt.title('Top 1 Products by Orders')
plt.show()


# In[41]:


# Found out all the id's and correponding occupation of customers 
# who buys those top 1 products from above analysis we found out that top 1 


# In[47]:


product_orders = df.groupby(['Product_ID', 'Product_Category'])['Orders'].sum()

# Get the top 10 products with the highest orders
top_10_products = product_orders.nlargest(10)

# Sort in descending order and plot as a bar graph
top_10_products.sort_values(ascending=False).plot(kind='bar')

# Get the names of the top 10 products
top_10_product_names = top_10_products.index.get_level_values('Product_Category')

# Print the names of the top 10 products
print("Names of the products with maximum orders:")
print(top_10_product_names)

plt.xlabel('Product ID')
plt.ylabel('Orders')
plt.title('Top 10 Products by Orders')
plt.show()


# # Conclusion:
# 
# ### Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




