#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_input(fibo):
    def newfunc():
        a=int(input("enter a number "))
        fibo(a)
    return newfunc()

    


# In[23]:


@get_input
def recur_fibo(a):
    def newfunc(a):
        if a <= 1:  
            return a  
        else:  
            return(newfunc(a-1) + newfunc(a-2))  
        if a <= 0:  
            print("Plese enter a positive integer")  
        else:  
            print("Fibonacci sequence:")  
    for i in range(a):  
        print(newfunc(i))  


# In[ ]:





# In[ ]:




