
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")



column=int(str(position[0])) -1
row=int(str(position[1])) - 1

map[row][column]='x'

print(f"{row1}\n{row2}\n{row3}")
