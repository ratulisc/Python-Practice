"""


1. You will be given two input . One is string which will be either "normal" or "square" . And a integer n.
if the input is normal you have to print first n number of the normal seris i.e 1 2 3 4 5 6 ...
else you have to print first n number of square seris i.e 1 4 9 16 25 36 49 ...


2. You are a waiter in a restaurent called "Tea Heaven" and you will serve tea for the customer. Now not all the customer are
willing to pay money.
Also some customer has come with family so they want more than one cup of tea.
Input:
first you will be given two integer n -> the number of customer, price -> price of each cup of tea
than there will be n line of input where will be one integer which is amount of money.
for each customer you have to print how many cup of tea he will get

"""
string = input("Please enter your string type: ")
n = int(input("Please enter your number range: "))
if string.lower()=='normal':
    for i in range(1,n+1):
        print(i)

elif string.lower()=='square':
    for i in range(1,):
        if(i*i<=n):
         print(i*i)







def Tea_Heaven():
    tea_price = int(input("Enter the price of tea: "))

    n = int(input("How many people have come including you?:  "))
    for i in range(1,n+1):
        money = int(input("How much money you will pay: "))
        cot = money//tea_price
        print(i,"no.customer will get",cot,"cup of tea.")

Tea_Heaven()