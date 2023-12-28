##Staircase
# Objective : Print staircase with "#" with lowest is n
# Ex : n = 3
# Staircase :   # 
               ##
              ###
def staircase(n):
    #looping from 1 because the top is 1
    for i in range(1,n+1):
        #print the staircase
        print((n-i)*' '+i*'#')
#testing
staircase(10)