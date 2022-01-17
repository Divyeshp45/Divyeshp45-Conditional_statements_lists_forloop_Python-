import random
n=input("enter the names of people seperated by comma and space\n")
names=n.split(",")
person=random.choice(names)
print(person +" is going to pay the bill")
