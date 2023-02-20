#!/usr/bin/env python
# coding: utf-8

# In[2]:


#PROGRAM FOR TAKING NUMBER FROM USER AND PRINTING THE GRADE
marks = int(input(" Please enter your marks: "))
if(marks > 90):
    print("A Grade")
elif(marks > 80):
    print("B Grade")
elif(marks > 70):
    print("C Grade")
elif(marks > 60):
    print("D Grade")
elif(marks > 40):
    print("E Grade")
else:
    print("Fail")


# In[3]:


import random
hidden=random.randrange(1, 201)
guess = int(input("please enter your guess"))
if(guess == hidden):
    print("Hit")
elif(guess > hidden):
    print("close by, u are a true indian fan")
else:
    print("not close u dont watch match that much")


# In[8]:





# In[7]:


#sir i tried this program 
from random import randint
L=int(input("whats the length of FB profile pic "))
N=int(input("enter no of pics  "))
if(1<=N<=15 and 1<=L<=100):
    for i in range(N):
        W=int(randint(1,100))
        H=int(randint(1,100))
        if(1<=W,H<=100):
            if(W<L or H<L):
                print("the pic no has (W,L): UPLOAD ANOTHER PIC ")
                else:
                    if(W==L):
                        print("the pic no has(W,L): ACCEPTED ")
                        else:
                            print("the pic no has(W,L): crop it ")
                            else:
                                print("enter valid length of pic and length of picture ")
                


# In[12]:



file=open("t1.txt","w")
file.write("i love FCS ")
print(text)
file.close()
file =open ("t1.txt","r")
text= file.read()
print(text)
file.close()


# In[ ]:




