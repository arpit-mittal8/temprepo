# 7) accept numbers till user enters 0 and display the total of all the numbers entered.
sum = 0
while True:
    n = int(input("Enter the number :"))
    if n == 0:
        break
    sum = sum + n

print("The sum of all the numbers is :",sum)
    


