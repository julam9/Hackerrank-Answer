##Diagonal Difference
# Objective : Calculate the absolute difference of sum of two diagonals (left and right) from a matrix
def diagonalDifference(arr):
    #define the left and right diagonal through list comprehensions
    diag1, diag2 = sum([arr[i][i] for i in range(len(arr))]), sum([arr[j-1][-j]for j in range(1,len(arr)+1)])    
    return abs(diag1-diag2)
