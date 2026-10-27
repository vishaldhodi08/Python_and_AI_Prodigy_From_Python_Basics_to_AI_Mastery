
# ACP: Count the Digits in a Number

num = int(input("Enter a number: "))

temp = abs(num)
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print("Total digits =", count)
