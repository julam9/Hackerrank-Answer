##Plus Minus
# Objective : Find the proportion of positive, negative, and 0 in an array
def plusMinus(arr):
    #initialize variables for positive, negative, and 0
    neg = 0 
    pos = 0 
    zero = 0 
    #looping to count freq
    for x in arr: 
        if x < 0: neg += 1 
        elif x > 0: pos += 1 
        else: zero += 1 
        #calculate ratio
        pos_ratio = pos/len(arr) 
        neg_ratio = neg/len(arr) 
        zero_ratio = zero/len(arr)
    print('%.6f' % pos_ratio) 
    print('%.6f' % neg_ratio) 
    print('%.6f' % zero_ratio)
    