##Compare the Triplets
# Objective : Compare the score of first and second array per element position. If the two not same, higher get 1, lower get 0. If equal, both got 0. Sum the score 
def compareTriplets(a, b):
    #define variables for score
    p1, p2 = 0, 0
    #compare the score and give the 1 or 0 based on conditions
    for x,y in zip(a, b):
        if x>y :
            p1+=1
        elif y>x:
            p2+=1
        else: 
            p1+=0
            p2+=0
    return [p1, p2]
