#!/usr/bin/env python
# coding: utf-8

# In[1]:


var = 19
type(var)


# In[4]:


var = 1.9
type(var)


# In[8]:


var1 = '19'
type(var1)


# In[6]:


name_var1='ram'
print(name_var1)


# In[19]:


var = 'rahul'
massage= '{} {} HOW ARE YOU'.format(var , name_var1)
print(massage)


# In[22]:


massage= f'{var} {name_var1} How Are you'
print(massage)


# In[29]:


msg='RAM,HOW ARE YOU'
print(msg.lower())
print(msg.upper())
print(msg.__len__())
print(len(msg))
print(msg.count('A'))
print(msg.find('HOW'))
print(msg[4])
print(msg[0:10])


# In[ ]:




