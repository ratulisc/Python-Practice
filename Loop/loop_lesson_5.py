"""
write a program that prints first n letter of folowing series:
1 2 4 8 16 32 64 ...
  current value =2* previous value
  first value=1

"""
n=int(input("Enter the number of terms you want to have: "))
current_value=1
previous_value=-1 # kono value nai
for i in range(n):
    print(current_value,end =" ") # prints 1
    previous_value=current_value
    current_value=current_value*2












