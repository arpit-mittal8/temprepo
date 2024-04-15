# 5)	accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc. 

marks = int(input("Enter your marks: "))

if marks < 40:
    print("Fail")
elif marks >= 40 and marks < 50:
    print("Third Class")
elif marks >= 50 and marks < 60:
    print("Second Class")
elif marks >= 60 and marks < 75:
    print("First Class")
else:
    print("Distinction")