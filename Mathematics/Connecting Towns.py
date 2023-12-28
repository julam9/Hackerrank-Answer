##Connecting Towns
# Objective : Given array of length n with content of # path from city 1 to city n, calculate number of path modulo 1234567
def connectingTowns(n, routes):
    a = 1
    for i in routes:
        a *= i
    return a%1234567 