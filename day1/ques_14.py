rows = 5
k = 2*rows-2
for i in range(rows):
    for j in range(k):
        print(end=" ")
    k = k-2
    for j in range(i+1):
        print("*", end=" ")
    print()