##Mini-Max Sum
# Objective : Find minimum and maximum sum from from 4 elements in the array
# Condition : Length of array is 5
def miniMaxSum(arr):
    #min result by subtracting sum of array to max elements
    #max result by subtracting sum of array to in elements
    return sum(arr)-max(arr), sum(arr)-min(arr)
#testing 
miniMaxSum([1,2,3,4,5,6])
