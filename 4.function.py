#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add():
    var1=int(input('enter first value:'))
    var2=int(input('enter 2nd value:'))
    var3=var1+var2
    print("sum= ", var3)
add()


# In[3]:


def sub(var1,var2):
    var3=var1-var2
    print("sub= ", var3)
sub(9,2)


    


# In[7]:


def multi():
    var1=int(input('enter first value:'))
    var2=int(input('enter 2nd value:'))
    var3=var1*var2
    return var3
var4=multi()
print('multi=', var4)


# In[8]:


def divison(var1,var2):
    var3=var1/var2
    return var3
var4=divison(15,3)
print("divison=",var4)


# In[ ]:




