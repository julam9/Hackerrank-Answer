##Summing the N Series 
# Objective : Define Tn = n^2 - (n-1)^2. Calculate Sn mod 10^9+7 where Sn = T1 + T2 + ..... + Tn 
def summingSeries(n):
    #using math trick, Sn could be simplify into n^2
    return n**2%(10**9+7)
#testing 
summingSeries(229137999)