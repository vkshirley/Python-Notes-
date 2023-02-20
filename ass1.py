#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# list and its default functions
#1)list append:-
a=["bee","moth"]
print(a)
a.append("ant")
print(a)


# In[2]:


#2)list extend:-
a = ["bee", "moth"]
print(a)
a.extend(["ant", "fly"])
print(a)


# In[3]:


#3)list insert:-
a = ["bee", "moth"]
print(a)
a.insert(0, "ant")
print(a)
a.insert(2, "fly")
print(a)


# In[4]:


#4)list remove:-
a = ["bee", "moth", "ant"]
print(a)
a.remove("moth")
print(a)


# In[5]:


#5)list pop
# Example 1: No index specified
a = ["bee", "moth", "ant"]
print(a)
a.pop()
print(a)


# In[6]:


#Index specified
a = ["bee", "moth", "ant"]
print(a)
a.pop(1)


# In[11]:


#list clear:-
a = ["bee", "moth", "ant"]
print(a)
a.clear()

print(a)


# In[12]:


#list index:-
a = ["bee", "ant", "moth", "ant"]
print(a.index("ant"))
print(a.index("ant", 2))


# In[13]:


#list count:-
a = ["bee", "ant", "moth", "ant"]
print(a.count("bee"))
print(a.count("ant"))
print(a.count(""))


# In[14]:


#list sort:-
a = [3,6,5,2,4,1]
a.sort()
print(a)

a = [3,6,5,2,4,1]
a.sort(reverse=True)
print(a)


# # 1)DICTIONARY clear
# d = {1: "lets upgrade", 2: "is good "}
# d.clear()

# In[16]:


#2)DICTIONARY get
dic = {"A":1, "B":2} 
print(dic.get("A")) 
print(dic.get("C")) 
print(dic.get("C","Not Found ! "))


# In[17]:


#3)DICTIONARY keys
Dictionary1 = {'A': 'Lets', 'B': 'up', 'C': 'Grade'} 
# Printing keys of dictionary 
print(Dictionary1.keys()) 
  
# Creating empty Dictionary 
empty_Dict1 = {} 
  
# Printing keys of Empty Dictionary 
print(empty_Dict1.keys())
  


# In[19]:


#4)DICTIONARY values

dictionary = {"rajesh": 2, "stive": 3, "vikram": 4} 
print(dictionary.values())    
dictionary = {"vaibhav": "5", "is ": "3", "Good": "5"} 
print(dictionary.values())


# In[20]:


#4)DICTIONARY pop
test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 } 
  
# Printing initial dict 
print ("The dictionary before deletion : " + str(test_dict)) 
  
# using pop to return and remove key-value pair. 
pop_ele = test_dict.pop('Akash') 
  
# Printing the value associated to popped key  
print ("Value associated to poppped key is : " + str(pop_ele)) 
  
# Printing dictionary after deletion 
print ("Dictionary after deletion is : " + str(test_dict))


# In[21]:


#5)DICTIONARY update
Dictionary1 = { 'A': 'vk', 'B': 'sk', } 
Dictionary2 = { 'B': 'Vaibhav' } 
  
# Dictionary before Updation 
print("Original Dictionary:") 
print(Dictionary1) 
  
# update the value of key 'B' 
Dictionary1.update(Dictionary2) 
print("Dictionary after updation:") 
print(Dictionary1) 


# # 1)SETS add
# sets = {'g', 'e', 'k'} 
#   
# # adding 's' 
# sets.add('s') 
# print('Letters are:', sets) 
#   
# # adding 's' again 
# sets.add('s') 
# print('Letters are:', sets)
# 
# 

# In[25]:


#2)SETS clear
sets = {'g', 'e', 'e', 'k', 's'} 
print('sets before clear:', sets) 
sets.clear() 
print('sets after clear:', sets)


# In[26]:


#3)SETS copy
set1 = {1, 2, 3, 4}  
  
# function to copy the set 
set2 = set1.copy()   
print(set2)


# In[27]:


#4)SETS difference
A = {10, 20, 30, 40, 80} 
B = {100, 30, 80, 40, 60} 
print (A.difference(B)) 
print (B.difference(A))


# In[28]:


S = {"ram", "rahim", "ajay", "rishav", "aakash"} 

#5)Sets pop  
# Popping three elements and printing them 
print(S.pop()) 
print(S.pop()) 
print(S.pop()) 
print("Updated set is", S)


# In[29]:


#6)Sets update
list1 = [1, 2, 3]  
list2 = [5, 6, 7]  
list3 = [10, 11, 12]  
set1 = set(list2)  
set2 = set(list1) 
set1.update(set2)
print(set1)  
set1.update(list3)  
print(set1) 


# # tuple 
# tup = ('python', 'is easy') 
# print(tup)
# 

# In[31]:


#concatenating 2 tuples 
  
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'is easy')
print(tuple1 + tuple2)


# In[32]:


thistuple = ("apple", "banana", "cherry")
print(thistuple)


# In[33]:


#index
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# In[34]:


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# In[35]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


# In[38]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","apple")
thistuple.count("apple")


# # string 
# 

# In[39]:


a = "Hello"
print(a)


# In[40]:


a="hello","hello","this ","is ","a","string"
print(a)
a.count("hello")


# In[41]:


b = "Hello, World!"
print(b[2:5])


# In[42]:


b = "Hello, World!"
print(b[-5:-2])


# In[43]:


a = "Hello, World!"
print(len(a))


# In[45]:


a = "HELLO, WORLD!"
print(a.lower())


# In[46]:


a = "Hello, World!"
print(a.upper())


# In[48]:


a = "Hello, World!"
print(a.replace("H", "L"))


# In[ ]:




