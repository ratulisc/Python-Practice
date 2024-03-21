"""
১ থেকে ৯ এর মধ্যে এমন কোন সংখ্যা আছে কিনা যা ৫ দ্বারা বিভাজ্য?। যদি বিভাজ্য হয় তাহলে প্রিন্ট করো True আর না হলে প্রিন্ট করো False
"""

check=False

for i in range(1,10):
    if i%5==0:
        check=True
        break




if check==True:
    print("True")
else :
    print("False")

