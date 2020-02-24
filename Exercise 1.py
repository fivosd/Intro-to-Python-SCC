#!/usr/bin/env python
# coding: utf-8

# In[19]:


list = [1,2,3,4,5,6,7,8,9,10]
inp = int(input("What are you looking for in the array? "))

if type(inp) is type(list[0]):
    for i in range(0,len(list)):
        if list[i] == inp:
            print("element found")
            break
else:
    print("The data types do not match")

