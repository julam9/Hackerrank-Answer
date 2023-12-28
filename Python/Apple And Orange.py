##Apple and Orange
# Objective : Given Sam house with certain width. There is apple and orange tree, orange and apple will fall at different points. Determine how many apple and orange which fall in Sam house
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #point where apple falls
    apple_fall = [a + apple for apple in apples]
    #point where orange falls
    orange_fall = [b + orange for orange in oranges]
    #count how many apple falls in sam house
    n_apple = [a1 for a1 in apple_fall if a1 in range(s,t+1)]
    #count how many orange falls in sam house
    n_orange = [o1 for o1 in orange_fall if o1 in range(s,t+1)]
    print(len(n_apple))
    print(len(n_orange)) 
#testing
countApplesAndOranges(4,6,1,1,[1,3,2],[2,3])