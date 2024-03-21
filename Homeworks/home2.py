"""
You are a waiter in a restaurant called "Tea Heaven" and you will serve tea for the customer. Now not all the customer are
willing to pay money.
Now this is tea heaven right? So you don't want any customer to go back without a cup of tea.
also some customer are very kind to give extra money. Now if any customer give extra money you will store the extra money.
if any customer give less money you will compensate his money from your fund if possible.
Now make the whole system using your favorite Python Language

"""
"""



1. Initialize tea price and fund, total people
2. take the tea price input and set fund as 0

3. now run a for loop
4. inside loop get input the money that customer will give
5. if he give some extra money serve him tea and store extra money to fund
6. if he give less money check if you have enough fund
7. if you dont have fund say sorry
8. other wise serve him tea and take the required extra money from the fund



"""




def Tea_Heaven():

    tea_price = int(input("Enter the price of tea: "))
    total_people = int(input("How many people will come?: "))
    fund = 0
    for i in range(1,total_people+1):
        money = int(input("How much money will you pay: "))
        if money>=tea_price:
            extra = money-tea_price
            print("You will get 1 cup of tea")
            fund += extra

        else:
            fund+=money
            if fund>=tea_price:
                print("You wil get one cup of tea")
                fund-=tea_price
            else:
                print("Sorry,our fund doesn't remain the tea price")
    print("Your fund remains",fund,"$")


Tea_Heaven()