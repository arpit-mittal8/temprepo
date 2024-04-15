# print the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *


rows = int(input("Enter the numbers of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()


