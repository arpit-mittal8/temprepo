# 10) display prime numbers from 3 to 30

for num in range(3, 31):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)