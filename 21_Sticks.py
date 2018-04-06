#This is very simple game of sticks. There are 21 sticks, 1st the user picks number of sticks between 1-4,
#then the 2nd picks sticks(1-4).Whoever will pick the last stick means 21st sticks will loose.
#then we will fine the case when the user will win the game:
sticks = 21
print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("whoever will take the last stick will loose.")

while True:
    print("stick left: ", sticks)
    sticks_taken_user1 = int(input("User1 pick sticks (1-4):"))
    sticks = sticks - sticks_taken_user1
    print(sticks)
    if sticks == 0:
        print("User1 Win..! ")
    sticks_taken_user2 = int(input("User2 pick sticks (1-4):"))
    sticks = sticks - sticks_taken_user2
    if sticks == 0:
        print("User2 win..")
        break
    print(sticks)