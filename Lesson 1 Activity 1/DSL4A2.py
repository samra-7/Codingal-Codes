# Python program to print a star pattern based on the number of rows specified by the user

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
