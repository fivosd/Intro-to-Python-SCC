#!/usr/bin/env python
# coding: utf-8

# In[9]:


operators = ['+', '-', '/', '*', '%', '^']
st = ''
st = input("What do you want to calculate?\n")
current = ''
for op in operators:
    if op in st:
        st = st.split(op)
        current = op
        break
        
        
if current is '+':
    print(int(st[0])+int(st[1]))
if current is '-':
    print(int(st[0])-int(st[1]))
if current is '/':
    print(int(st[0])/int(st[1]))
if current is '*':
    print(int(st[0])*int(st[1]))
if current is '%':
    print(int(st[0])/int(st[1]))
if current is '^':
    print(int(st[0])**int(st[1]))

