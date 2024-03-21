###Question: ATM Cash Withdrawal

#Write a program that simulates an ATM cash withdrawal process. The program should take the desired withdrawal amount and
#check if it is within the available balance. The program should perform the following steps:

#1.Set the available balance in the account to $1000.
#2.Prompt the user to enter the withdrawal amount.
#3.Check if the withdrawal amount is within the available balance using an if-else statement.
#.If the withdrawal amount is less than or equal to the available balance, proceed to step 4.
#.If the withdrawal amount is greater than the available balance, display an error message and end the program.
#4.Deduct the withdrawal amount from the available balance.
#5.Display a success message along with the remaining balance.
#Note:

#Assume that the user will always enter a valid numerical value for the withdrawal amount.
#Ensure that the remaining balance is updated correctly after a successful withdrawal.
#You can assume that the ATM has an unlimited supply of cash and does not need to manage physical cash.



##Solution:

Available_Balance = 1000
Withdrawal_Amount= int(input("Please enter your Withdrawal Amount: $"))
if Withdrawal_Amount<=Available_Balance:
    print("Withdrawal successful. Remaining balance:",(Available_Balance-Withdrawal_Amount),"$")

else:
    print("Insufficient balance. Withdrawal amount exceeds the available balance.")


