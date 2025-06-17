#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
path_to_file = 'shared/homeworks/python_ds_miniprojects/2/bookings.csv'
bookings = pd.read_csv(path_to_file, sep = ';')
bookings_head = bookings[0:7]


# In[2]:


bookings


# In[3]:


bookings.dtypes


# In[4]:


rename_columns = {}
for col in bookings.columns:
    rename_columns[col] = col.replace(' ','_').lower()


# rename_columns

# In[5]:


bookings = bookings.rename(columns=rename_columns)


# In[6]:


bookings


# In[7]:


cv=bookings.query("is_canceled = ='0'")


# In[8]:


cv


# In[9]:


cv['country'].value_counts()


# In[10]:


bookings['stays_total_nights'] = bookings['stays_in_weekend_nights'] + bookings['stays_in_week_nights']


# In[11]:


bookings['stays_total_nights']


# In[12]:


bookings.groupby('hotel', as_index = False).aggregate({'stays_total_nights':'mean'}).round(2)


# In[13]:


bookings['reserved_room_type']!=bookings['assigned_room_type']


# In[14]:


bookings['ravno_neravno']=bookings['reserved_room_type']!=bookings['assigned_room_type']


# In[15]:


bookings['ravno_neravno'].value_counts()


# In[ ]:





# In[16]:


bookings2016 = bookings.query("arrival_date_year == '2016'")


# In[17]:


bookings2016['arrival_date_month'].value_counts()


# In[18]:


bookings2017 = bookings.query("arrival_date_year == '2017'")


# In[19]:


bookings2017['arrival_date_month'].value_counts()


# In[20]:


bookings_ch_canceled= bookings.query("hotel == 'City Hotel'").query("is_canceled == '1'")


# In[21]:


bookings_ch_canceled


# In[22]:


bookings_ch_canceled.query("arrival_date_year == '2015'")['arrival_date_month'].value_counts()


# In[23]:


bookings_ch_canceled.query("arrival_date_year == '2016'")['arrival_date_month'].value_counts()


# In[24]:


bookings_ch_canceled.query("arrival_date_year == '2017'")['arrival_date_month'].value_counts()


# In[25]:


bookings


# In[26]:


bookings.aggregate({'children':'mean'})


# In[27]:


bookings.aggregate({'babies':'mean'})


# In[28]:


bookings.aggregate({'adults':'mean'})


# In[29]:


bookings['total_kids']= bookings['babies'] +bookings['children']


# In[30]:


bookings


# In[31]:


bookings.groupby('hotel', as_index = False).aggregate({'total_kids':'mean'}).round(2)


# In[32]:


bookings['has_kids'] = bookings['total_kids'] >= 1


# In[57]:


bookings.groupby('has_kids',as_index=False)    .aggregate({'lead_time':'count', 'is_canceled':'sum'})    .rename(columns={'lead_time':'bookings_count'})


# In[58]:


bookings_kids = bookings.groupby('has_kids',as_index=False)    .aggregate({'lead_time':'count', 'is_canceled':'sum'})    .rename(columns={'lead_time':'bookings_count'})


# In[63]:


bookings_kids['churn_rate'] = round(bookings_kids['is_canceled'] / bookings_kids['bookings_count'], 4) * 100


# In[66]:


bookings_kids


# In[87]:


bookings.groupby('has_kids', as_index=False).agg(is_canceled=('is_canceled', 'sum'), bookings_count=('is_canceled', 'count'))


# In[92]:


bookings.groupby('has_kids', as_index=False).agg({'is_canceled':'count'}).loc[0][1]


# In[68]:


bookings['is_canceled'].value_counts()


# In[35]:


canceled_bookings = bookings['is_canceled'].value_counts()[1]


# In[36]:


bookings.aggregate({'is_canceled':'count'})


# In[37]:


churn_rate = (canceled_bookings/bookings.aggregate({'is_canceled':'count'})).round(4)


# In[38]:


churn_rate


# In[50]:


#bookings.query("is_canceled == '1' and has_kids == True")


# In[40]:


cb = bookings.query("is_canceled == '1'")


# In[41]:


cb


# In[42]:


cb.query("has_kids == True")['is_canceled'].value_counts()


# In[43]:


cb.query("has_kids == True")['is_canceled'].value_counts()[1]


# In[44]:


churn_rate_with_child = (cb.query("has_kids == True")['is_canceled'].value_counts()[1]/bookings.aggregate({'is_canceled':'count'})).round(4)


# In[45]:


churn_rate_with_child


# In[46]:


cb.query("has_kids == False")['is_canceled'].value_counts()


# In[47]:


cb.query("has_kids == False")['is_canceled'].value_counts()[1]


# In[ ]:





# In[ ]:




