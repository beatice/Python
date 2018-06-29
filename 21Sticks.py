#!/usr/bin/env python3
import random
stick = 21
i = 1
print("There are 21 sticks. Each round, you and the computer will take 1-4 sticks in turn, whoever take the last stick will lose the game.")

while stick > 0:
    if i == 1:    
        print('"21 sticks" start!')
    
    print("*" * 50)
    print("Round ", i)
    print("Sticks left: ", stick)

    while True:
        user = int(input("Please enter the number of sticks (1-4) you want to take: "))
        if 1 <= user <= 4:
            if user == 1:
                print("You will take {} stick.".format(user)) 
            else:
                print("You will take {} sticks.".format(user))  
            stick -= user
            break
        else:
            print("The number is out of range")
            continue

    if stick <= 0:
        print("Oops, you take the last stick, game lost. Do you want to try again?")
        reply = input('reply "Y" for play again, reply "N" for quit: ')
        if reply == "Y":
            stick = 21
            i = 1
            continue
        else:
            break
    
    print()
    print("Sticks left: ", stick)
    computer = random.randint(1,4)
    if computer == 1:
        print("The computer will take {} stick.".format(computer)) 
    else:
        print("The computer will take {} sticks.".format(computer))    
    stick -= computer

    if stick <= 0:
        print("Congraduation! The computer take the last stick, you won. Do you want to try again?")
        reply = input('reply "Y" for another round, reply "N" for quit: ')
        if reply == "Y":
            stick = 21
            i = 1
            continue
        else:
            break
    
    i += 1
