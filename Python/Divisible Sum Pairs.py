##Divisible Sum Pairs
# Objective : Find i,j from intager array where i < j and i+j is divisible by integer k
def divisibleSumPairs(n, k, ar):
    #initialize result
    n=0
    #looping for first index
    for i in range(0, 6):
        #looping for second index
        for j in range(1, 6):
            #check if i<j and sum of two elements divisible by k
            if (i<j) and (ar[i]+ar[j])%k==0:
                n=n+1
#testing function
divisibleSumPairs(6, 3, [1,3,2,6,1,2])