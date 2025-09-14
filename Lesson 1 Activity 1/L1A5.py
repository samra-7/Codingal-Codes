print("Check your is between 10 to 20 years or not")
x = int(input("enter your age: "))


if x > 10: #condition 1
  print("Your age is more than 10 years")
  if x > 20: #nested condition
    print("And it is more than 20 as well")
  else:
    print("But it is less not more than 20")