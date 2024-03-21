"""

"""

string = input("Please,enter a string: ")
length= len(string)
if(length<2): print("Empty string")
else:
    new_string=''
    new_string+=string[0]
    new_string+=string[1]
    new_string+=string[length-2]
    new_string+=string[length-1]
    print(new_string)