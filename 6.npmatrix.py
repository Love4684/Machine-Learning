#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
my_list = [1,2,3,4,5]
type(np.array(my_list))
arr = np.array(my_list)
arr


# In[22]:


np.random.seed(101)
arr=np.random.randint(0,100,10)
print(arr)
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.argmax())


# In[27]:


map = np.arange(0,100).reshape(10,10)
map


# In[29]:


map = np.arange(0,100).reshape(10,10)
print(map[0,:])
map[0:3,0:3]


# In[ ]:




