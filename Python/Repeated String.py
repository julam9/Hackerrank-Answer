##Repeated String 
# Objective : Calculate the occurences of "a" letter from a word that is made of multiple of s and limited to n
def repeatedString(s,n):
    #frequency of original a in original string
    ans = s.count('a') 
    #conditional if 10 is divisible by the length of original string
    if n%len(s)==0 :
        #freq of "a" letter times how many times original string repeated
        ans = ans*(n//len(s)) 
    #conditional if 10 is not divisible by the length of original string    
    else : 
        #freq of "a" letter times how many original string repeated plus freq of "a" letter in the rest of string
        ans =  ans*(n//len(s)) + s[:n%len(s)].count('a') 
    return ans