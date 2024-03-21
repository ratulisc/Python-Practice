print("Enter 1 for Review")
print("Enter 2 for Bug")
print("Enter 3 for Developer")
Question_NO = int(input("Please enter your Question number: "))

if Question_NO == 1:
    print("Rate My Game From 1-10: ")
    Review_rating = int(input("please enter your rated number: "))
    if Review_rating>=7:
        print("Thanks for your Rating")
    else:
        input("Game_Developer: what can we improve??")

        print("Thanks for your valuable suggestion")

if Question_NO == 2:
    Bug=input("Please tell me what is the bug in my game? ")

    print("Thanks for pointing that", Bug)
    print("We will fix it soon")

if Question_NO == 3:
    print("What is your study Background?")
    Study_Backround = input("please Enter your study backround: ")
    if Study_Backround=="CSE":
        print("You can Join in our company,But let us know how much salary do you want?")
        Expected_Money = int(input("Please enter your Expected money: "))
        if Expected_Money <= 100:
            print('You can join here from tomorrow')
        else:
            print("Sorry,you expected much money.")
    else:
        print("Sorry,We cant take you in our company!")
