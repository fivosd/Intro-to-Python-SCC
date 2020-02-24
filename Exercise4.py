#!/usr/bin/env python
# coding: utf-8

# In[14]:


names = ["Brad","Tom","Jane","Kyle","Anna"]
companies = ["Goldman Sachs","HSBC","JP Morgan", "Deutsche Bank", "Bank of America"]
salaries = [120,85,235,92,110]

for i in range(0,len(names)):
    print(names[i],"works at:",companies[i],"and makes:",salaries[i],"k")


# In[ ]:


name_temp = input("name: ")
company_temp = input("company: ")
salary_temp = int(input("salary: "))
names.append(name_temp)
companies.append(company_temp)
salaries.append(salary_temp)


# In[15]:


position = 0
del_who = input("Which one do you want to delete? ")
for i in range(0,len(names)):
    if names[i] is del_who:
        position = i
        names.pop(i)
        companies.pop(i)
        salaries.pop(i)
        
        

for i in range(0,len(names)):
    print(names[i],"works at:",companies[i],"and makes:",salaries[i],"k")

