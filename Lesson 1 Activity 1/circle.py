n=int(input("enter a number"))
counter=0
temp=n
while temp!=0:
    digit=temp%10
    counter+=1
    temp=temp//10
print("total digits are ",counter)    

    
