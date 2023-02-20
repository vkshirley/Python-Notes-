#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter number of chances you want a user to upload ?"))

l = int(input("Enter the min Length ?"))

curent_operation = 0
while(curent_operation<n):
    curent_operation += 1
    
    h = int(input("Enter ur Height of photo ?"))
    w = int(input("Enter ur Width of the photo ?"))
    
    if ( h >= l and w >=l):
        if(h==w):
            print("Accepted")
        else:
            print("Crop it")
    else:
        print("minimum photo size should be - ", l )


# In[ ]:


x = 0 
y = 0 

max_move = 0

while(max_move <= 5):
    max_move += 1
    command = input("Enter the Command for ankit to move - ")
    command = command.lower()
    
    if(command == "l"):
        x += -1
    elif (command == "r"):
        x += +1
    elif (command == "u"):
        y += 1
    elif( command == "d"):
        y -= 1
    else: 
        print("Enter valid input, L,R,U,D")
    
    print("ankit is here - ", x, y)


# In[ ]:




