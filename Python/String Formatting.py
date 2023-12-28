##String Formatting
# Objective : Given n, print the decimal, octal, hexadecimal (cappitalized), binary of each value from 1 to n
def print_formatted(n):
    for i in range(1, n+1):
        print(i, int(oct(i)), hex(i), bin(i))
#testing 
print_formatted(4)