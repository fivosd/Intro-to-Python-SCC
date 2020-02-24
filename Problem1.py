#!/usr/bin/env python
# coding: utf-8

# In[4]:


names = ["a","b","c","d","e"]

phonebook = {
    'a' : 12,
    'b' : 22,
    'c' : 32,
    'd' : 42,
    'e' : 52,
}

for i in names:
    print(i)

query = input("name: ")

if query in phonebook:
    print(phonebook[query])
else:
    print("It doesn't exits")

