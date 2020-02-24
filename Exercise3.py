#!/usr/bin/env python
# coding: utf-8

# In[2]:


times = [9.6,11.6,12.8,9.9,9.7,15.9,13.1,10.1,10.3,10.2]
worst = [0,0,0]

times.sort()
times.reverse()

for i in range(0,3):
    worst[i] = times[i]

for i in worst:
    print(i)
    times.remove(i)

