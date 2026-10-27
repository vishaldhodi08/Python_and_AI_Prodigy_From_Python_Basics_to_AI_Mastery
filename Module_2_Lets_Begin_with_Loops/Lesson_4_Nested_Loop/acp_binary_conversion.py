
# ACP: Decimal to Binary Conversion

decimal = int(input("Enter a decimal number: "))

if decimal == 0:
    binary = "0"
else:
    binary = ""

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

print("Binary number =", binary)
