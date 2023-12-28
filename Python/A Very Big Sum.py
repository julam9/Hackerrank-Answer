##A Very Big Sum
# Objective : Calculate sum of an array which could contain a quite large integer
def aVeryBigSum(ar):
    sumarr = 0
    #looping through array and sum each element
    for i in ar:
        sumarr += int(i)
    return sumarr