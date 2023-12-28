##Between Two Sets 
# Objective : Given two array integers, determine number of integers that satisfy conditions
# Conditions :
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
def getTotalX(a, b):
    a1 = 0
    #loopint through max of first array and minimum of second array (inclusive)
    #Why?
    #Because max first array and min second array is the range of value that could satisfy the conditions
    for i in range(max(a), min(b)+1):
        if all(i % el == 0 for el in a) and all(el % i == 0 for el in b):
            a1 = a1 + 1
    return a1
#testing
getTotalX([2,4], [16,32,96])