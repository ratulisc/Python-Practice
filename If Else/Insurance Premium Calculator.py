###Question: Insurance Premium Calculator

#Write a program that calculates the insurance premium for a customer based on their age and driving experience. The program should consider the following criteria:

#If the customer is below 25 years old, they are considered a young driver.

#Young drivers with less than 2 years of driving experience pay a premium rate of $500.
#Young drivers with 2 or more years of driving experience pay a premium rate of $300.

#If the customer is 25 years old or above, they are considered an adult driver.

#Adult drivers with less than 5 years of driving experience pay a premium rate of $400.
#Adult drivers with 5 or more years of driving experience pay a premium rate of $200.
#Write a Python program that takes the customer's age and driving experience (in years) as input, and calculates and displays the insurance premium they need to pay.

#Your program should perform the following steps:

#Prompt the user to enter their age.
#Prompt the user to enter their driving experience in years.
#Based on the age and driving experience, calculate the insurance premium using if-else statements.
#Display the calculated insurance premium to the user.

#Assume that the user will always enter valid numerical values for age and driving experience.


###Solution ::

age = int(input("Please enter your age: "))
driving_experience = int(input("Enter your driving experience in year: "))
if age<25:
    if driving_experience<2:
        print("Your insurance premium is 500$")
    else:
        print("Your insurance premium is 300$")

else:
    if driving_experience<5:
        print("Your insurance premium is 400$")
    else:
        print("Your insurance premium is 200$")