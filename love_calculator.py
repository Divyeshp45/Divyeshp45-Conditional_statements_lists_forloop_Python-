print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1=name1.lower()
name2=name2.lower()
name_1=name1.count('t')+name1.count('r')+name1.count('u')+name1.count('e')+name2.count('t')+name2.count('r')+name2.count('u')+name2.count('e')

name_2=name1.count('l')+name1.count('o')+name1.count('v')+name1.count('e')+name2.count('l')+name2.count('o')+name2.count('v')+name2.count('e')


total=str(name_1)+str(name_2)
print(f"{total}")


total1=int(total)
if total1<10 and total1>90 :
    print(f"Your score is {total},you go together like coke and mentos.")
elif total1>40 and total1<50 :
    print(f"Your score is {total},you are alright together.")
else:
    print(f"Your score is {total}.")   