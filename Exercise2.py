#!/usr/bin/env python
# coding: utf-8

# In[3]:


items = ["Car","House","Cat"]


while 0 < 1:
    new_item = ""
    new_item = input("What is the new item you have? ")
    if new_item == "Kill":
        break
    items.append(new_item)
    print("You now have:",len(items),"Items")

