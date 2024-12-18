#1.
rows = 7  # Number of rows

for i in range(rows, 0, -1):
    print('*' * i)

#2.
rows = 5  # Number of rows

for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)

#3.
    rows = 5  # Number of rows

for i in range(1, rows + 1):
    pattern = ""
    for j in range(1, i + 1):
        pattern += str(j % 2)  # Alternate between 1 and 0
    print(pattern)
#4.
rows = 5  # Number of rows

for i in range(1, rows + 1):
    # Create spaces for right alignment
    spaces = ' ' * (rows - i)
    # Generate the binary pattern for the current row
    pattern = ''.join(str((i + j) % 2) for j in range(i))
                       # Print the combined result
    print(spaces + pattern)
#5.

rows = 5  # Number of rows

for i in range(rows):
    # Add leading spaces
    spaces = ' ' * i
    # Add stars decreasing in number
    stars = '*' * (2 * (rows - i) - 1)
    # Print the combined result
    print(spaces + stars)

