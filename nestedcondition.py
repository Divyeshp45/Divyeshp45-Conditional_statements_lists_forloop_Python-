#HERE WE SEE NESTED CONDITION ELIF LADDER
print("WELCOME TO ESSEL WORLD! :)")
height=input("ENTER YOUR HEIGHT : ")
height_1=int(height)


if height_1 >=123:
    print("YOU CAN ENJOY THIS RIDE :)")
    age=int(input("ENTER YOUR AGE :  "))
    if age<12 :
        print("YOU HAVE TO PAY 20 RUPEES")
       
    elif age<18 :
        print("YOU HAVE TO PAY 30 RUPEES")
    elif age>45 and age<55:
        print("You have to pay 0 Rupees")
               
    else :
        print("YOU HAVE TO PAY 50 RUPEES")     


else :
    print("SORRY  YOU CANNOT ENTER :(")    
 