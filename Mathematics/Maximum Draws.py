##Maximum Draws
# Objective : Find the minimum draws to find a matching pair color of socks from n socks 
# Conditions : There are two cases,
# - there are n colors
# - there are t colors, t < n 
def maximumDraws(n):
    #for first case, after n draws, the next drawed color must be has pair with any drawed color
    #for second case, same as the first case but with t color
    return n+1
    #only return 1 value because the input is multiple line 