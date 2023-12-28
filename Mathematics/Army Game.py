##Army Game
# Objective : Given square with n rows and m columns, determine minimum # of packages need to be sent to supply all the boxes
# Ilustration : https://www.hackerrank.com/challenges/game-with-cells/problem?isFullScreen=true 
import math

def gameWithCells(n, m):
    #case if it 1x1
    if n == 1 and m == 1 :
        ans = 1
    
    elif n ==m :
        ans = (n-1)*(m-1)
    elif (n==1 or n==2) and m > 1: 
        ans = m-1 
    elif (m==1 or m==2) and n > 1 :
        ans = n-1 
    else :
        ans = (n-1)*(m-1)
    return ans