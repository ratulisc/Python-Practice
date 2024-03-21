"""

Question: BMI Calculator and Classification
Write a program that calculates the Body Mass Index (BMI) of a person based on their height and weight. The
program should then classify the BMI into different categories according to the following criteria:

BMI less than 18.5: Underweight
BMI 18.5 to 24.9: Normal weight
BMI 25 to 29.9: Overweight
BMI 30 or greater: Obesity
The formula to calculate BMI is BMI = weight / (height * height), where weight is in kilograms and height is in
meters.

"""

height1 = int(input("Please enter your height in feet: "))
height2 = (height1*12*2.54)/100
weight = int(input("Please enter your Weight in KG: "))
BMI = weight / (height2 * height2)

if (BMI<18.5):
    print("Uderweight")

elif(BMI==18.5 and BMI<=24.9):
    print("Normal Weight")

elif(BMI==25 and BMI<=29.9):
    print("Overweight")

else:
    print("Obesity")