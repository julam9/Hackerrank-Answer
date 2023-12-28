##Number Line Jumps
# Objective : Given 2 kangoroos start point and jump, determine if the kangaroo will meet at one point
def kangaroo(x1, v1, x2, v2):
    answer = ''
    #if kang 2 start ahead of kang 1 and jump kang 2 less than kang 1, determine if the distance is reachable
    if x1<x2 and v1>v2:
        diff=v1-v2
        dist=x2-x1
        answer = 'YES' if dist%diff==0 else 'NO'
    #if kang 1 start ahead of kang 2 and jump kang 1 less than kang 2, determine if the distance is reachable
    elif x1>x2 and v1<v2:
        diff=v2-v1
        dist=x1-x2
        answer = 'YES' if dist%diff==0 else 'NO'    
    #if the start and jump of one kang is ahead than other kang 
    elif (x1>x2 and v1>v2) or (x1<x2 and v1<v2) or (x1==x2 and v1!=v2) or (x1!=x2 and v1==v2): answer = 'NO'
    else: answer='YES' 
    return answer
#testing
kangaroo(1,2,1,1)   