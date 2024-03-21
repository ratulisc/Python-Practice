"""

You have make a game. Now people are asking you some question. Now, they have 3 type of question:
1.Review
2.Bug
3.Developer
if they choose review you will ask what will you give our game out of 10. If he gives more than 7, say thanks
otherwise ask him what can we improve. take the feedback and say thanks.

if they choose Bug ask them what bug they have found. take their feedback and say thanks

if they choose developer ask which subject he studies in. if he is from any other subject than cse tell him that
we cant take him in our team. otherwise if he is from cse ask him what is his expected salary
if his expected salary is less than 100 take him in . otherwise tell him that we cant let you in

"""
##Solution:

#Game_Developer = Ratul
#Questioner = Munim
def playGame():
    Question_Type = input("Please Enter Your Question Type: ")

    if Question_Type == "Review":
        print("Rate My Game From 1-10: ")
        Review_rating = int(input("please enter your rated number: "))
        if Review_rating >= 7:
            print("Thanks for your Rating")
        else:
            input("Game_Developer: what can we improve??")

            print("Thanks for your valuable suggestion")

    if Question_Type == "Bug":
        Bug = input("Please tell me what is the bug in my game? ")

        print("Thanks for pointing that", Bug)
        print("We will fix it soon")

    if Question_Type == "Developer":
        print("What is your study Background?")
        Study_Backround = input("please Enter your study backround: ")
        if Study_Backround == "CSE":
            print("You can Join in our company,But let us know how much salary do you want?")
            Expected_Money = int(input("Please enter your Expected money: "))
            if Expected_Money <= 100:
                print('You can join here from tomorrow')
            else:
                print("Sorry,you expected much money.")
        else:
            print("Sorry,We cant take you in our company!")


playGame()
print("Thanks")
playGame()
print("hi")
playGame()
print("100")
