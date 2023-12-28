##Leonardo's prime factor 
# Objective : Given n, count the maximum number of distinct prime factors of any number in the inclusive range 
def primeCOunt(n):
    prime = 2
    if n==1:
        return 0
    else :
        prime = prime + 1
        if prime%any(2,3,5,7,9)!=0:
            return 1