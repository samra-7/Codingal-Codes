num = int(input("Enter a number: "))

t = num
numlen = 0

# Count the number of digits
while t > 0:
    numlen += 1
    t = t // 10

if numlen >= 4:
    half = numlen // 2
    chk = 0
    midone = 0
    midtwo = 0

    # Extract middle two digits from right
    while chk <= half:
        rem = num % 10

        if chk == half:
            midone = rem
        elif chk == half - 1:
            midtwo = rem

        num = num // 10
        chk += 1

    print("Product of middle two digits:", midone * midtwo)

else:
    print("Number is not 4 digits long.")
