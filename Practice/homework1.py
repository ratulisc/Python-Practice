"""
Theif Detector:

You are going on a long vacation, so you want to set up a theif detector on your door .
If anyone ring bells on the door your program will ask him few question. if he can answer properly
he will be able to enter. otherwise you will tell him that he is a thief and door will remain close.
Here are the questions:
1. Are you a human? ->
and should be yes.
2. what is Ratul's favorite color:
ans should be black or white,


3. what is your age?
if age is greater than 40 it is ok.

"""


def theif_detector():
    qa = input("Are you a human? ")
    if qa == "Yes" or qa == "yes":
        color = input("What is Ratul's favorite color? ")
        if color == "black" or color =="Black" or color =="White" or color =="white":
            age = int(input("Please enter your age: "))
            if age > 40:
                print("The door is open. ")
            else:
                print("The door is closed")
        else:
            print("The door is closed")
    else:
        print("The door is closed")


theif_detector()



