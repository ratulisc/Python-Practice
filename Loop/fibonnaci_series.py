"""

print the first n number of famous fibonacci series
 1 1 2 3 5 8 13 21

current_value=previous_value+second_previous_value
first_value=1
second_value=1

"""
n=int(input("How many terms you want? "))


current_value=1
previous_value=0
second_previous_value=0

for i in range(n):

    print(current_value,end=" ")

    #update
    second_previous_value=previous_value
    previous_value=current_value
    current_value=second_previous_value+previous_value



