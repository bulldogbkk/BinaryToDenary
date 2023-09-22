# Declare variables
binarynumber = input("Please enter a binary number (1s and 0s only): ")
value = 0
placevalue = 0

# Calculate placevalue
for i in range(len(binarynumber)):
    placevalue = 2 ** (len(binarynumber)-1)

# Convert binary to decimal
for i in range(len(binarynumber)):
    if binarynumber[i] == '1':
        value += placevalue
        placevalue //= 2
    elif binarynumber[i] == '0':
        placevalue //= 2

# Output the result
print("The value in denary is", value)
