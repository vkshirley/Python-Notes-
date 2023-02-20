
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




import random
hidden=random.randrange(1, 201)
guess = int(input("please enter your guess"))
if(guess == hidden):
    print("Hit")
elif(guess > hidden):
    print("close by u are a true indian fan")
else:
    print("not close u dont watch match that much")

