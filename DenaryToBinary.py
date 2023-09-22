# Declare variables
num = int(input("Please input a denary number to be converted into binary: "))
answer = ""

# Repeat until num is less than 1
while num >= 1:
    if num % 2 == 0:
        digit = '0'
    else:
        digit = '1'
    answer = digit + answer
    num = num // 2  # Integer division in Python 3

# Output the result
print("Your number in binary is:", answer)
