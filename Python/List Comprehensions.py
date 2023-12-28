##List Comprehensions
# Objective : Input three integers. Make all combinations of elements from range 0 to three integers and the sum is not equal to n 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input()) 
       
    #list comprehension to make a list
    a1 = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    #filter the list to desired condition
    a2 = [el for el in a1 if sum(el) != n]
    print(a2)