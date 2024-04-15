# File 13 in day1 folder

rows = int(input("Enter number pf rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()