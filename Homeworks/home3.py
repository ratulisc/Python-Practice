"""
You are the owner of the store Electronics Khutinati. Everyday in your shop many people give you message to ask
the price of your product. Also customer are very annyoing. Often they start bargaining for no reason.
But unfortunately you are a very busy person. You are mostly busy with your academics .
But you are genius too. So you are thinking to set up a automated AI system that will answer customers question and
bargein with them.

Input:
first you will ask customer question what kind of watch he want. there are 3 type of watch.
1. premium
2. Good
3. Average
The base price of all your product is 1000 tk. If it is premium price will increase by 3. if good price will increase by
2 and if average price will remain 500 taka .
Then you will ask what kind of build he want. there are 3 type of build in your store.
1. Bangladeshi Build.
2. Japanese build
3. chinese build
so if the build is japanese price will increase by two again , if the build is bangladeshi price will increase by 1.5
otherwise price will remain same.
Now also you will ask if the watch is for a boy or a girl. if for boy the price will increase by 3 and if girl
price will increase by 2

Then Bargeining!
Now you give a price. now the customer will give his price . so if his price is around 200 tk of your price you
will give him the product otherwise you will kick him out.


"""

type = input("What type of Watch you Want?: ")
build = input("What kind of build you want?: ")
gender = input("For which gender the watch is?: ")
price = 1000
if type == "Premium" or type == "premium":
    price = price*3
elif type == "good":
    price = price*2
elif type == "average":
    price = price


if build == "Bangladeshi":
    price = price*1.5
elif build == "Japanese":
    price = price*2
elif build == "Chinese":
    price = price

if gender == "boy":
    price = price*3
elif gender == "girl":
    price = price*2


print("Your watch costs ",price,"$")

bargain = int(input("Please tell me your last price: "))
if price-bargain <= 200:
    print("Take your watch.")
else:
    print("Sorry,We can't sell this in insufficient money.")

