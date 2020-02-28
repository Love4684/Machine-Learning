#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[5]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('our first plot')
plt.show()


# In[9]:


import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.0,2.0,0.01)
s=1+np.cos(2*np.pi*t)
plt.plot(t,s,"r")
plt.grid()
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.title("cosine wave plot(xos(x))")
plt.show()


# In[13]:


import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)
plt.subplot(2,1,1)
plt.plot(x1,y1,'o-')
plt.title('subplot-1')
plt.xlabel('x1')
plt.ylabel('ampy1')

plt.subplot(2,1,2)
plt.plot(x2,y2,'-')
plt.title('subplot-2')
plt.xlabel('x2')
plt.ylabel('ampy2')

plt.show()


# In[25]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,24,30,20,15]
tick_label=['one','two','three','four','five']
plt.bar(x,y,tick_label=tick_label,width=0.7,color=['green','blue'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('bar graph')
plt.show()


# In[33]:


import matplotlib.pyplot as plt
age=[20,30,10,40,28,39,29,59,40,44,69,80,
     85,44,49,29,35,55,65,88,85,75]
range=(0,100)
bins=10
plt.hist(age,bins,range,color='green')
plt.xlabel('age')
plt.ylabel('bins')
plt.title('histogram  graph')
plt.show()


# In[37]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,5,6,8,9,1,3,12,14]
plt.scatter(x,y,label='star',color='green',marker='*',s=30)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('scatter plot')
plt.legend()
plt.show()


# In[53]:


import matplotlib.pyplot as plt
iteam=['eat','sleep','work','play']
slice=[3,7,8,6]
color=['r','g','m','b']
plt.pie(slice,labels=iteam,colors=color,startangle=90,shadow=True,explode=(0.2,0,0,0.1),autopct='%1.2f%%')
plt.legend()
plt.show()


# In[56]:


import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,2*np.pi,0.01)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,label='sin')
plt.plot(x,y2,label='cosine')
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('sin and cosin')
plt.show()


# In[58]:


import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open ('test.txt','r') as csvfile:
    plots=csv.reader(csvfile)
    for col in plots:
        x.append(col[0])
        y.append(col[1])
plt.plot(x,y,label='file')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('test graph')
plt.legend()
plt.show()


# In[61]:


import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open ('test1.csv','r') as csvfile:
    plots=csv.reader(csvfile)
    for col in plots:
        x.append(col[0])
        y.append(col[1])
plt.plot(x,y,label='file')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('test graph')
plt.legend()
plt.show()


# In[ ]:




