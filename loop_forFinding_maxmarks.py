marks=input("enter the marks of students:\n").split()
for n in range(0,len(marks)) :
    marks[n]=int(marks[n])
highest_score=0
for num in marks:
    if num>highest_score:
        highest_score=num

print(highest_score)