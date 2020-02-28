#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
data=[5,3,6,8,2,9]
pd.Series(data)


# In[ ]:





# In[9]:


import pandas as pd
data=[5,3,6,8,2,9]
s=pd.Series(data) #method()
print("sum=",s.sum())
s.values #attribute
#s.index


# In[11]:


import pandas as pd
fruits=['Apple','banana','mango','watermelon']
weekdays=['son','mon','tue','wed']
pd.Series(data=fruits,index=weekdays)


# In[14]:


import pandas as pd
pd.read_csv("test1.csv")


# In[15]:


import pandas as pd
pd.read_csv("test1.csv",squeeze=True,usecols=['value'])


# In[52]:


import pandas as pd
values=pd.read_csv("test1.csv",squeeze=True,usecols=['value'])
values.head()


# In[53]:


print(value.values)
print(value.is_unique)
print(value.ndim)
print(value.shape)


# In[29]:


import pandas as pd
data=pd.read_csv("test1.csv",squeeze=True,usecols=['value'])
print(data.sort_values())
print(data.sort_values().head())


# In[34]:


import pandas as pd
data=pd.read_csv("test1.csv",squeeze=True,usecols=['value'])
print(data.sort_values(ascending=False))
print(data.head())


# In[37]:


import pandas as pd
data=pd.read_csv("test1.csv",squeeze=True,usecols=['value'])
print(data.sort_values(ascending=False,inplace=True))
print(data.head())


# In[49]:


import pandas as pd
idx=pd.read_csv("test1.csv",squeeze=True,usecols=['index'])
print(idx.sort_index(ascending=False))
print(idx.sort_index(ascending=False,inplace=True))
print(idx.head())


# In[51]:


import pandas as pd
values=pd.read_csv("test1.csv",squeeze=True,usecols=['value'])
print(values)
print(values[5])
print(values[2:6])
print(values[[3,2,1]])


# In[77]:


#index label
import pandas as pd 
print(pd.read_csv("test1.csv"))
data=pd.read_csv("test1.csv",index_col="index",squeeze=True)
print(data)
print(data.sort_index(inplace=True))
print(data[10])
print(data.get([4,7]))
print(data.get(6))


# import pandas as pd
# 

# In[6]:


import pandas as pd
MathData=pd.read_csv("test1.csv",squeeze=True,usecols=['value'])
print(MathData)
print(MathData.value_counts())
data=MathData.head()
print(data)
print(MathData.mean())
print(data.mean())
print(MathData.idxmax())
print(MathData.max())


# In[9]:


import pandas as pd 
print(pd.read_csv("test1.csv"))
data=pd.read_csv("test1.csv",index_col="index",squeeze=True)
print(data)
print(data.value_counts())
print(data.value_counts().sum(),data.count())


# In[16]:


import pandas as pd
data=pd.read_csv("test1.csv",squeeze=True,index_col="index")


# In[ ]:





# In[18]:


def perform(number):
    if number > 10:
        print("number is greater than ten")
    elif number >= 5 and number <= 10:
        print('number is between 5 and 10')
    else: 
        print('number is less than ten')


# In[19]:


data.apply(perform)


# In[23]:


import pandas as pd
data=pd.read_csv("test1.csv",squeeze=True,usecols=['value'])
print(data)
def perform(number):
    if number > 10:
        return "number is greater than ten"
    elif number >= 5 and number <= 10:
        return 'number is between 5 and 10'
    else: 
        return 'number is less than five'
data.apply(perform)


# In[25]:


import pandas as pd
data=pd.read_csv("test1.csv",squeeze=True,index_col="index")
print(data)
data.apply(lambda value:value+1)


# In[ ]:




