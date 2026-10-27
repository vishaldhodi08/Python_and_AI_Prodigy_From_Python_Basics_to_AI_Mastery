# Function to calculate squares and separate odd/even squares

def square_numbers(start, end):
    squares = []

    for number in range(start, end + 1):
        squares.append(number ** 2)

    return squares


# Take range input from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start > end:
    print("Invalid range! Starting number must be less than or equal to ending number.")
else:
    squares = square_numbers(start, end)

    # Separate odd and even squares
    odd_squares = []
    even_squares = []

    for square in squares:
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("All square values:", squares)
    print("Odd square values:", odd_squares)
    print("Even square values:", even_squares)