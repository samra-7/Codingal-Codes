rowNum = 5 #initialised number of rows 5
space = rowNum-1

for i in range(1, rowNum+1): #loops for rows
  for j in range(1, space+1): #loop for space 
    print(end=" ")
  space = space-1
  
  for j in range(2*i-1): #loop for upper part of diamond
    print(end="*")
  print()
space = 1
#loops for lower part of diamond
for i in range(1, rowNum):
  for j in range(1, space+1):
    print(end=" ")
  space = space+1
  for j in range(1, 2*(rowNum-i)): 
    print(end="*")
  print()
