#name=input("enter \n")
#print("gm ,"+name)
        
letter=''' Dear <|Name|> ,
Iam happy to inform that you have been selected to google .
Have a nice day.
REGARDS 
Date: <|Date|>
'''
name =input("Enter name\n")
date  =input("Enter date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)

