n = int (input("Enter the number of terms: "))
current_value = 1
previous_value = 0
second_previous_value = 0
for i in range(n):
    print(current_value,end=' ')

    second_previous_value = previous_value
    previous_value = current_value
    current_value = second_previous_value + previous_value 