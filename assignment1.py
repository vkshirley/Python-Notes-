#list and its default functions
#1)list append:-
a=["bee","moth"]
print(a)
a.append("ant")
print(a)

#2)list extend:-
a = ["bee", "moth"]
print(a)
a.extend(["ant", "fly"])
print(a)


#3)list insert:-
a = ["bee", "moth"]
print(a)
a.insert(0, "ant")
print(a)
a.insert(2, "fly")
print(a)

#3)list remove:-
a = ["bee", "moth", "ant"]
print(a)
a.remove("moth")
print(a)


#5)list pop
# Example 1: No index specified
a = ["bee", "moth", "ant"]
print(a)
a.pop()
print(a)

# Example 2: Index specified
a = ["bee", "moth", "ant"]
print(a)
a.pop(1)


#5)list clear:-
a = ["bee", "moth", "ant"]
print(a)
a.clear()

print(a)


#6) list index:-
a = ["bee", "ant", "moth", "ant"]
print(a.index("ant"))
print(a.index("ant", 2))


#7)list count:-
a = ["bee", "ant", "moth", "ant"]
print(a.count("bee"))
print(a.count("ant"))
print(a.count(""))



#8)list sort:-
a = [3,6,5,2,4,1]
a.sort()
print(a)

a = [3,6,5,2,4,1]
a.sort(reverse=True)
print(a)


#1)DICTIONARY clear
d = {1: "geeks", 2: "for"}
d.clear()

#2)DICTIONARY get
dic = {"A":1, "B":2} 
print(dic.get("A")) 
print(dic.get("C")) 
print(dic.get("C","Not Found ! "))



#3)DICTIONARY keys
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'} 
  
# Printing keys of dictionary 
print(Dictionary1.keys()) 
  
# Creating empty Dictionary 
empty_Dict1 = {} 
  
# Printing keys of Empty Dictionary 
print(empty_Dict1.keys())




#4)DICTIONARY values

dictionary = {"raj": 2, "striver": 3, "vikram": 4} 
print(dictionary.values())    
dictionary = {"geeks": "5", "for": "3", "Geeks": "5"} 
print(dictionary.values())  



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


#5)DICTIONARY update
Dictionary1 = { 'A': 'Geeks', 'B': 'For', } 
Dictionary2 = { 'B': 'Geeks' } 
  
# Dictionary before Updation 
print("Original Dictionary:") 
print(Dictionary1) 
  
# update the value of key 'B' 
Dictionary1.update(Dictionary2) 
print("Dictionary after updation:") 
print(Dictionary1) 


#1)SETS add
GEEK = {'g', 'e', 'k'} 
  
# adding 's' 
GEEK.add('s') 
print('Letters are:', GEEK) 
  
# adding 's' again 
GEEK.add('s') 
print('Letters are:', GEEK)

#2)SETS clear
GEEK = {'g', 'e', 'e', 'k', 's'} 
print('GEEK before clear:', GEEK) 
GEEK.clear() 
print('GEEK after clear:', GEEK)

#3)SETS copy
set1 = {1, 2, 3, 4}  
  
# function to copy the set 
set2 = set1.copy()   
print(set2)


#4)SETS difference
A = {10, 20, 30, 40, 80} 
B = {100, 30, 80, 40, 60} 
print (A.difference(B)) 
print (B.difference(A))


S = {"ram", "rahim", "ajay", "rishav", "aakash"} 

#5)Sets pop  
# Popping three elements and printing them 
print(S.pop()) 
print(S.pop()) 
print(S.pop()) 
print("Updated set is", S)


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











