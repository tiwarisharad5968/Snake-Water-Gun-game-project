'''
Snake = 1
Water = -1
Gun = 0

'''
import random

Computer = random.choice([1, -1, 0])
YourChoice = input("Enter Your Choice: ")
YourDict = {"S": 1, "W": -1, "G": 0 }
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

You = YourDict.get(YourChoice)

#By now we have got two Variables/Numbers, You and Computer

if(You == Computer):
    print("It's Draw!")

else:
    if(Computer == 1 and You == -1):
        print("You Win!")

    elif(Computer == 1 and You == 0):
        print("You Lose!")

    elif(Computer == -1 and You == 1):
        print("You Lose!")

    elif(Computer == -1 and You == 0):
        print("You Win!")

    elif(Computer == 0 and You == 1):
        print("You Win!")

    elif(Computer == 0 and You == -1):
        print("You Lose!")

    else:
        print("Invalid Input")