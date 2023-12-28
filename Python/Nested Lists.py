##Nested Lists
# Objective : Given students and their grades, find students whose grade is second lowest
# Condition : If there are more than 1 student, print alphabetically
if __name__ == '__main__':
    #array to placing name and score
    a1=[]
    a2=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a1.append([name, score])
        a2.append(score)
    #find second lowest grade (after sorted in set (disctinct) way, second lowest is on index 1)        
    ans = sorted(list(set(a2)))[1]  
    for i,j in sorted(a1):
        if j == ans:
            print(i)
