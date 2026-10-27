
# Activity 3: Reverse Order

# Input a number greater than 1
n = int(input("Enter the value of n: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    print("Numbers from {} to 1 are:".format(n, 1))

    # Loop to print numbers in reverse order
    for i in range(n, 0, -1):
        print(i)
