"""
you have a number. find the length of the number
1234 -> len=4
2112 -> len=4
2112 /10 =211
211/10 =21
21/10 =2
2/10 =0
"""
n=int(input("Please enter a number: "))


counter=0
while n>0:
    n=int(n/10)
    counter+=1

print("Number of digit is ",counter)




