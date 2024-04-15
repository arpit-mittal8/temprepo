# File 15 in day1 folder


rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()