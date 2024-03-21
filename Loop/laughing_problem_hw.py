"""
Problem: Counting Chuckles
You have just attended a comedy show and want to count the number of times the audience laughed during the performance.
However, the comedian's jokes were  so funny that people laughed different numbers of times after each joke.
Your task is to count the total number of laughs by summing up the laughter counts.

Write a program that prompts the user to enter the number of jokes and then asks for the number of laughs after each joke.
Finally, calculate and display the total number of laughs.

Here's an example of the expected input and output:

Input:
Enter the number of jokes: 4
Enter the number of laughs after joke 1: 5
Enter the number of laughs after joke 2: 3
Enter the number of laughs after joke 3: 7
Enter the number of laughs after joke 4: 2

Output:
Total number of laughs: 17

Remember to use loops to iterate through each joke and accumulate the total number of laughs using if-else statements.
 Make it fun and interesting!
"""
num=int(input("Enter the number of jokes: "))
sum=0
for i in range(1,num+1):
    print("Enter the number of laughs after joke: ",i)
    laugh= int(input())
    sum+=laugh

print("Total number of laughs: ",sum)




