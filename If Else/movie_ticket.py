"""
Question: Ticket Price Calculation (with discounts)
A movie theater charges different ticket prices based on the age and the day of the week.
 Write a program that takes the age of a person and the day of the week
  as input and determines the ticket price based on the following criteria:

Children (age 0-12) pay $8 on weekdays and $10 on weekends.
Teenagers (age 13-17) pay $10 on weekdays and $12 on weekends.
Adults (age 18 and above) pay $12 on weekdays and $15 on weekends.
Additionally, there is a 10% discount on ticket prices for senior citizens (age 65 and above) on weekdays only.
The program should calculate and print the ticket price for the given age and day of the week, taking into account the discounts.

"""

#Solution:

age = int(input("Please Enter your age: "))
day = input("Enter the current day: ")

if age>=0 and age<=12:
    if day == "friday":
        print("Ticket price = 10$")
    else:
        print('Ticket Price = 8$')

elif age>=13 and age<=17:
    if day == "friday":
        print("Ticket price = 12$")
    else:
        print('Ticket Price = 10$')

elif age>=18 and age<65:
    if day == "friday":
        print("Ticket price = 15$")
    else:
        print('Ticket Price = 12$')

elif day == "friday" and age>=65:
    discount=15*(10/100)
    discounted_price= 15-discount
    print(discounted_price,"$")

else:
    discount = 12 * (10 / 100)
    discounted_price = 12 - discount
    print(discounted_price,"$")