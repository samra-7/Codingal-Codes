ch = input("Please Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
  #check the alphabat
    print("The Given Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'): 
  #check the digit
    print("The Given Character ", ch, "is a Digit")
else: 
  #check the character other than character and digit
    print("The Given Character ", ch, "is a Special Character")