#!/usr/bin/env python
# coding: utf-8

# In[4]:


try:
    file=open("vk.txt",'r')
    file.write("exception")
except Exception as e:
    print("the file gave the error---- ",e)
    file=open("vk.txt",'r')
    print(file.read())
finally:
    file.close()


# In[5]:


get_ipython().system('pip install pylint')


# In[9]:


def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))


# In[8]:


test_prime(2)


# In[10]:


get_ipython().run_cell_magic('writefile', 'prime.py', 'def test_prime(n):\n    if (n==1):\n        return False\n    elif (n==2):\n        return True;\n    else:\n        for x in range(2,n):\n            if(n % x==0):\n                return False\n        return True             \nprint(test_prime(9))')


# In[11]:


import unittest
import prime

class test(unittest.TestCase):
    def test_one(self):
        n=2
        result= prime.test_prime(n)
        self.assertEqual(result,'Python')
    def test_two(self):
        n=4
        result= prime.test_prime(n)
        self.assertEqual(result,'Python')
if __name__ == '__main__':
    unittest.main()


# In[ ]:




