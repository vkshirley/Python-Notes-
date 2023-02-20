#QUESTION1
a=input("TYPE STRING HERE:")
a=a.upper()
count=0
a1=["A", "D", "O", "P", "R"]
for i in a:
  for j in a1:
    if i==j:
      count+=1
      continue
  if i=="B":
    count+=2
print(count,end="")





#todays work
#file handling
f=open("t1.txt",'w')
print(f.write("hello world\n"))
print(f.write("how are you"))
print(f.read())

print(f.open("t1.txt",'a'))
print(f.write("WELCOME TO MY WORLD DUDE/n"))
print(f.readline())
f.close()


#os.rename(currentname,newname)
import os
os.rename("t1.txt","t2.txt")
print("renamed succesfully")


a=1
b=2
c=a+b
print(c)
str1="a="+st(a)+"\n"
str2="b="+st(b)+"\n"
str1="c="+st(c)+"\n"
f=open("t1.txt",'w')
f.write(str1)
f.write(str2)
f.write(str3)
f.close()
print("data saved to file successfully")
print(f.closed)


import os
os.mkdir("pycharm")
print("directory created succesfully")

os.getcwd()
os.rmdir("pycharm")
print("directory removed succefully ")

os.listdir()



#try except
try:
    a=int(input("enter a no:"))
    b=int(input("enter a no:"))
    c=a/b
    print(c)
except Exception:
    print("something is wrong")


try:
    a=int(input("enter a no:"))
    b=int(input("enter a no:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("divide by 0 is not possible.try again")
except ValueError:
    print("please enter numeric values.try again")


    
#using while loop    
while True:
    try:
        a=int(input("enter a no:"))
        b=int(input("enter a no:"))
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("divide by 0 is not possible.try again")
    except ValueError:
        print("please enter numeric values.try again")

     
#using try-except else

try:
    a=int(input("enter a no:"))
    b=int(input("enter a no:"))
    c=a/b
except:
    print("something is wrong")
else:
    print("answer is:",c)


#except with multiple attributes

try:
    x=int(input("enter a no:"))
    ans=100/x
except(ValueError,ZeroDivisionError):
    print("something is wrong")
else:
    print("answer is:",ans)
    
                
                
#try-finally
    
    
try:
    x=int(input("enter a no:"))
    ans=100/x
except(ValueError,ZeroDivisionError):
    print("something is wrong")
else:
    print("answer is:",ans)
finally:
    print("end of program")



#MAP
def sqr(a):
    return a*a
x=map(sqr,[1,2,3,4])
print(x)
print(list(x))

        
#with multiple arguments
def sqr(a,b):
    return a*b
x=map(sqr,[1,2,3,4],[5,6,7,8])
print(x)
print(list(x))



#LAMBDA FUNCTIONS
x=lambda a:a*a
x(3)


def abc(x):
    return lambda y:x+y
t=abc(4)
print(t)
print(t(5))



    
    


 





