n=int(input("enter the number of rows: "))

#iterate loop for row
for i in range(n):
  #loop for columns
    for j in range(n):
        if j == i:
          print(i, j)