"""
You are in a strange world. This is a very dangerous world. In this world you have to be very careful to be alive.
You were walking through the road and a team of gangster attacked you and forced you to play a game. If you fail
this game you will die. So here is the rule:
1. First you will be given a number and you have say if is it even or odd.if you fail to answer correctly
YOU WILL DIE IMMEIDEATELY. Otherwise you will continue to play
2. You will given two number and have to say which is the minimum between these two. And once again:
 if you fail to answer correctly
YOU WILL DIE IMMEIDEATELY. Otherwise you will continue to play
3. You will be given a string and you have to print that string thrice and then print your name+that string and then print
"I want to live"
4. If you complete these three task succesfully you will be free otherwise DIE.
"""

#####Solution:
def play_game():
    # Task 1: Check if the number is even or odd
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


    # Task 2: Find the minimum between two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    minimum = min(num1, num2)
    print("Minimum number:", minimum)
    # Task 3: Manipulate strings
    string = input("Enter a string: ")
    print(string * 3)
    print("Your name + string:", "YourName" + string)
    print("I want to live")

    # Check if all tasks were completed successfully
    print("Congratulations! You completed the game and survived.")


# Start the game
play_game()