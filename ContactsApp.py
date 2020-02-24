#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#keys array serves as a user readable (printable) list of the fields
keys = ["first name", "surname", "phone", "school"]
#empty arrays to be populated later
contacts = []
person = {}

# infinte loop
while 0 < 1:
    # creating a menu
    print("\n")
    print("Welcome to Dict Contacts 1.0")
    print("1: View Contacts")
    print("2: Add Contacts")
    print("3: Delete Contacts")
    print("4: Shutdown")
    menu_1 = int(input(":"))
    # we can use a Switch here but I like the IF more

    if menu_1 is 1:
        print("\n")
        for i in range(0,len(contacts)):
            print(i,":",contacts[i].get('first name'))
        menu_view = int(input("Which contact do you want to view: "))
        print("\n")
        for i in keys:
            print(i,":",contacts[menu_view].get(i))
        

    if menu_1 is 2:
        print("\n")
        for i in keys:
            # print out the filed name
            inp = input(i)
            # creates a new filed with Key = i & Entry = inp
            person[i] = inp

        contacts.append(person)
        #
        person = {}

    if menu_1 is 3:
        print("\n")
        for i in range(0,len(contacts)):
            print(i,":",contacts[i].get('first name'))
        menu_del = int(input("Which contact do you want to delete: "))
        contacts.pop(menu_del)
        print("Done.")
    
    if menu_1 is 4:
        break


# In[ ]:




