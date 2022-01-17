import random


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num=(len(names))
print(type(num))
choice=random.randint(0,num)
print(choice)

print(f"{names[choice]} is going to buy dinner today") 
