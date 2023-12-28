##Migratory Birds
# Objective : Find type of bird which has highest frequency. If there is more than 1 type, print the lowest type 
def migratoryBirds(arr):
    #initialize variable for max freq
    n=0
    #looping for freq of each element of an array
    for el in set(arr):
        #checking if freq is more than max freq
        if arr.count(el)>n:
            n=arr.count(el)
        #answer equal to element whose freq is the max freq
            answer=el         
    return answer  