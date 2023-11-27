##Solve me first
# Objective : Calculate the sum of two integers
def solveMeFirst(a,b):
    return a+b

##Simple array sum
# Objective : Calculate the sum of elements in an array
def simpleArraySum(ar):
    #use the python sum function
    return sum(ar)

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

##A Very Big Sum
# Objective : Calculate sum of an array which could contain a quite large integer
def aVeryBigSum(ar):
    sumarr = 0
    #looping through array and sum each element
    for i in ar:
        sumarr += int(i)
    return sumarr

##Diagonal Difference
# Objective : Calculate the absolute difference of sum of two diagonals (left and right) from a matrix
def diagonalDifference(arr):
    #define the left and right diagonal through list comprehensions
    diag1, diag2 = sum([arr[i][i] for i in range(len(arr))]), sum([arr[j-1][-j]for j in range(1,len(arr)+1)])    
    return abs(diag1-diag2)

##Caesar cipher
# Objective : Find the word with new alphabet order. For the non-letter character, return as it is
def caesarcipher(s, k) :
    orig='abcdefghijklmnopqrstuvwxyz'
    #define new alphabet order
    new=orig[k:]+orig[:k]
    #capitalize each letter on original alphabet
    orig_upper = orig.upper()
    #capitalize new order of alphabet
    new_upper=new.upper()
    #transform from original to new order
    changer = orig.maketrans(orig, new)
    #transform too but for the capital letter
    upper_changer = orig_upper.maketrans(orig_upper, new_upper)
    answer=[]
    #looping through letter
    for j in s:
        if j.islower()==True:
            #if the letter is in lowercase
            answer.append(j.translate(changer))
        elif j.isupper()==True:
            #if the letter is in uppercase
            answer.append(j.translate(upper_changer))
        #if the character is not letter, ex: "-", ",", "/", etc
        else : answer.append(j)
    #from array to string
    answer = ''.join(map(str, answer)) 
    return answer

##Repeated String 
# Objective : Calculate the occurences of "a" letter from a word that is made of multiple of s and limited to n
def repeatedString(s,n):
    #frequency of original a in original string
    ans = s.count('a') 
    #conditional if 10 is divisible by the length of original string
    if n%len(s)==0 :
        #freq of "a" letter times how many times original string repeated
        ans = ans*(n//len(s)) 
    #conditional if 10 is not divisible by the length of original string    
    else : 
        #freq of "a" letter times how many original string repeated plus freq of "a" letter in the rest of string
        ans =  ans*(n//len(s)) + s[:n%len(s)].count('a') 
    return ans

##Jumping on the clouds
# Objective : Get to the finish position through clouds (0 : safe, 1 : not safe). Find the shortest path (minimum # of jumps)
# Condition : 
# - Maximal jump is 2
# - First cloud and last cloud (finish cloud) is 0 
def jumpingOnClouds(c):
    #index and step definition
    i=0
    step=0
    #looping while the position is not on finish yet
    while i < len(c) - 1 :
        #check if next cloud is 1
        if c[i+1] == 1 :
            #if yes, then the next two clouds must be 0
            i=i+2
        #check if next cloud is 0
        elif c[i+1] == 0 :
            #check if next two coluds is the finish
            if i+2<len(c)-1 and c[i+2]==0:
                i=i+2
            else : i=i+1
        step = step + 1
    return step

##Divisible Sum Pairs
# Objective : Find i,j from intager array where i < j and i+j is divisible by integer k
def divisibleSumPairs(n, k, ar):
    #initialize result
    n=0
    #looping for first index
    for i in range(0, 6):
        #looping for second index
        for j in range(1, 6):
            #check if i<j and sum of two elements divisible by k
            if (i<j) and (ar[i]+ar[j])%k==0:
                n=n+1
#testing function
divisibleSumPairs(6, 3, [1,3,2,6,1,2])

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
    
##Staircase
# Objective : Print staircase with "#" with lowest is n
# Ex : n = 3
# Staircase :   # 
               ##
              ###
def staircase(n):
    #looping from 1 because the top is 1
    for i in range(1,n+1):
        #print the staircase
        print((n-i)*' '+i*'#')
#testing
staircase(10)

##Mini-Max Sum
# Objective : Find minimum and maximum sum from from 4 elements in the array
# Condition : Length of array is 5
def miniMaxSum(arr):
    #min result by subtracting sum of array to max elements
    #max result by subtracting sum of array to in elements
    return sum(arr)-max(arr), sum(arr)-min(arr)
#testing 
miniMaxSum([1,2,3,4,5,6])

##Breaking the Records
# Objective : Given Maria record of point scored, determine how many times Maria breaks her record for most and least points during the season
def breakingRecords(scores):
    n = len(scores)
    #how many times max scored breaked
    max_record = [scores[i+1] for i in range(n-1) if max(scores[:i+1]) < scores[i+1]]
    #hwo many times min scored breaked
    min_record = [scores[i+1] for i in range(n-1) if min(scores[:i+1]) > scores[i+1]]
    return(len(max_record), len(min_record))    
#testing 
breakingRecords([1,10,5,1,6,99,100,101,5])

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

##Grading Students
# Objective : Round the original grade to final grade
# Conditions :
#- Under 40 wont be rounded
#- If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#- If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade
def gradingStudents(grades):
    return [g+(g > 37)*(g % 5 > 2)*(5 - (g % 5)) for g in grades] 
#testing
gradingStudents([38,39,40,41,42])

##Time Conversion
# Objective : Given 12 hour format, change to 24 hour format
def timeConversion(s):
    #check if in am
    if s[-2:] == 'AM':
      #special case where the time is 12:00
      if s[0:2] == '12':
        tc_result = str(s.replace('12', '00', 1))
      else : tc_result = s
    #check if in pm
    if s[-2:] == 'PM' :
      #special case where the time is 24:00
      if s[0:2] != '12':     
        tc_result = str(int(s[0:2])+12)+s[2:]
      else : tc_result = s
    return tc_result[:8]
#testing
timeConversion('01:00:09PM')

##Birthday Cake
# Return the freq of candles whose height is max height
def birthdayCakeCandles(candles):
    return candles.count(max(candles))
#testing
birthdayCakeCandles([2,3,4,5,5])

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