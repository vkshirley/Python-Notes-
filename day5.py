#!/usr/bin/env python
# coding: utf-8

# In[ ]:



class Bank_Account: 
	def __init__(self): 
		self.balance=0
		print("this is vk's bank ") 

	def deposit(self): 
		amount=float(input("Enter amount to be Deposited: ")) 
		self.balance += amount 
		print("\n Amount Deposited:",amount) 

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\n You Withdraw:", amount) 
		else: 
			print("\n Insufficient balance ") 

	def display(self): 
		print("\n Net Available Balance=",self.balance) 


s = Bank_Account() 

s.deposit() 
s.withdraw() 
s.display() 


# In[ ]:


import math
class cone():
    def __init__(self,radius):
        self.radius=radius
        
    def area(self,r,s):
        return pi * r * s + pi * r * r 
    def vol(self):
        return (1 / 3) * pi * r * r * h 

radius = float(5) 
height = float(12) 
slat_height = float(13) 
obj=cone(r)
print("surface Area of cone:",round(obj.area(),2))
print("vol of circle:",round(obj.vol(),2))
        











