##Jumping on the clouds
# Objective : Get to the finish position through clouds (0 : safe, 1 : not safe). Find the shortest path (minimum # of jumps)
# Condition : 
# - Maximal jump is 2
# - First cloud and last cloud (finish cloud) is 0 
def jumpingOnClouds(c):
    #index and step definition
    i=0
    step=0
    n=len(c)
    #looping while the position is not on finish yet
    while i < n-1 :
        #check if next two clouds not passing finish cloud and next two clouds is 0 (safe)
        if i + 2 < n - 1 and c[i+2] == 0:
            #add index and step
            i = i + 2
            step = step + 1
        #check if next two clouds not passing finish cloud and next two clouds is 1 (not safe)
        elif i + 2 < n - 1 and c[i+2] == 1:
            #add index and step
            i = i + 1
            step = step + 1
        #if two conditions above not met
        else :
            i = i + 2 
            step = step + 1
    return step
#testing
jumpingOnClouds([0,0,0,0,1,0])