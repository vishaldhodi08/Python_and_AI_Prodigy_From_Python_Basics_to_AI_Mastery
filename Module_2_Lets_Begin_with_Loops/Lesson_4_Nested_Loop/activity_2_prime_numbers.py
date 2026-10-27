
# Activity 2: Print Prime Numbers in a Range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers are:")

for num in range(max(2, start), end + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()
