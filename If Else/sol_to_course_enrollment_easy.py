year=int(input("Please enter your study year: "))
course=input("Which course do you want to enroll: ")

if(year==1):
    if(course=="CSE"):
        print("Eligible for enrollment.")
    else:
        print("Not eligible for enrollment.")

elif (year==2):
    print("Eligible for enrollment.")

elif (year==3):
    if(course=="CSE" or course=="ECE"):
        print("Eligible for enrollment.")
    else:
        print("Not eligible for enrollment")

else :
    print("Eligible for enrollment.")
