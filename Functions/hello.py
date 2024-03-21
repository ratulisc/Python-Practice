"""

স্কুলে ১০০ নাম্বারের বাড়ির কাজ দেওয়া হয়েছে, এখন ১০০ তে ৪০ এর নিচে পেলে ফেইল, ৪০ হতে ৮০ পেলে মোটামুটি এবং ৮০ থেকে ১০০ পেলে এক্সিলেন্ট এবং যারা ৮০ থেকে ১০০ পাবে তাদেরকে হচ্ছে টাকা গিফট দিবে।
এখন কত টাকা চাও সেটা তুমিই ইনপুট দিবে। যদি তোমার টাকার পরিমান ১০০০ টাকার সমান বা কম হয় তোমাকে দিবে আর না হলে বলবে যে অতিরিক্ত চাচ্ছো।

"""

Exam_Number=100
Acheived_Number=int(input("Please enter your Acheived Number: "))

if(Acheived_Number<=40):
    print(" You failed in this class.")

elif(Acheived_Number>40 and Acheived_Number<=80):
    print(" Your grade is Average.")

elif(Acheived_Number > 100):
    print("Wrong Input")

else:
    print("Welcome,Your marks of all subjects are Excellent")

if Acheived_Number >= 80 and Acheived_Number <= 100:
    print("Congratulations! You will receive a gift of money.")

    Expecting_Money=int(input("Give Your Expected Money:"))
    if Expecting_Money<=1000:
        print("You will get the money soon.")
    else:
        print("Sorry,we can't afford this money.")