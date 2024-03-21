Year = int(input("Please enter a year: "))
if Year%4!=0:
    print("No")
else:
    if Year%100!=0:
        print("Yes")
    else:
        if Year%400!=0:
            print("No")
        else:
            print("Yes")


