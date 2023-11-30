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

##Between Two Sets 
# Objective : Given two array integers, determine number of integers that satisfy conditions
# Conditions :
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
def getTotalX(a, b):
    a1 = 0
    #loopint through max of first array and minimum of second array (inclusive)
    #Why?
    #Because max first array and min second array is the range of value that could satisfy the conditions
    for i in range(max(a), min(b)+1):
        if all(i % el == 0 for el in a) and all(el % i == 0 for el in b):
            a1 = a1 + 1
    return a1
#testing
getTotalX([2,4], [16,32,96])

##Finding the Percentage
# Objective : Given the student's name and their scores, find the average of scores based on stundet's name input
# Condition : Result in format of 2 decimal places
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a1 = {n:s for (n,s) in student_marks.items() if n==query_name}
    print("{:.2f}".format(sum(a1[query_name])/len(a1[query_name])))

##Tuples
# Objective : Using hash function (built in function), find the hash of tuple given 
# Conditions : Only work on Pypy3 
if __name__ == '__main__':
    #input
    n = int(input())
    #list of input
    integer_list = map(int, input().split())
    #make list as tuple   
    tuple_list = tuple(integer_list)
    print(hash(tuple_list))

##sWAP cASE
# Objective : convert lowercase to uppercase and vice versa in a string
def swap_case(s):
    #variable to store new string
    new_string = ''
    #looping thorugh character
    for i in s:
        #check is it in lowercase
        if i.islower() == True :
            #change to uppercase
            new_string = new_string + i.upper()
        #check is it in uppercase
        elif i.isupper() == True :
            #change to lowercase
            new_string = new_string + i.lower()
        else : 
            #just let character as it is
            new_string = new_string + i
    return new_string
    
##Text Wrap 
# Objective : Given string S and width w, wrap the sting into paragraph of width w
# Example : 
# S = abcdefgh
# w = 2 
# Desired output : 
# ab
# cd
# ef
# gh
def wrap(string, max_width):
    n=len(string)
    #for index which is helpful
    i=0
    #check if width is still more than string length
    while n > max_width:
        #print the desired output
        print(string[i:max_width+i])
        #to make string smaller
        n=n-max_width
        #moving the index to new location
        i=i+max_width
        #check if remain strings length is less than width
        if n < max_width:
            #print remain strings
            return(string[i:])
        
##Lists 
# Objective : Do some operations on the list
# Conditions : Elements added must be integer
if __name__ == '__main__':
    #initialize N
    N = int(input())
    #ans list
    ans = []
    #looping until N commands
    for i in range(N):
        k = input().split()
        #matching the command
        match(k[0]):
            case "insert":
                ans.insert(int(k[1]), int(k[2]))
            case "print":
                print(ans)
            case "remove":
                ans.remove(int(k[1]))
            case "append":
                ans.append(int(k[1]))
            case "sort":
                ans.sort()
            case "pop":
                ans.pop()
            case "reverse":
                ans.reverse()
                
##String split and join
# Objective : Given a string, split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    #split first and then join
    return "-".join(line.split(" "))
      
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
##What's your name?
# Objective : Given first and last name, print the first and last name in desired format
def print_full_name(first, last):
    #using string format
    print("Hello {0} {1}! You just delved into python.".format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

##Mutations
# Objective : Given a string, change the character at a given index and then print the modified string
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
##Find a string
# Objective : Find how many substring present in a string
def count_substring(string, sub_string):
    #variables for count
    cnt = 0
    #looping through string
    for i in range(0, len(string)):
        #check if the part of string equal to sub_string
        if string[i:len(sub_string)+i] == sub_string:
            cnt += 1
        else : cnt += 0
    return cnt
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
##String Validators
# Objective : Given a string, check if the sring contain alphanumeric, alphabetical, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    #using list comprehension to check every element
    print(True if True in [True for x in s if x.isalnum()] else False)
    print(True if True in [True for x in s if x.isalpha()] else False)
    print(True if True in [True for x in s if x.isdigit()] else False)
    print(True if True in [True for x in s if x.islower()] else False)
    print(True if True in [True for x in s if x.isupper()] else False)
    
##Text Alignment
# Objective : Replace __ (blank) with rjust/ljust/center to make logo
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


##String Formatting
# Objective : Given n, print the decimal, octal, hexadecimal (cappitalized), binary of each value from 1 to n
def print_formatted(n):
    for i in range(1, n+1):
        print(i, int(oct(i)), hex(i), bin(i))
#testing 
print_formatted(4)

##Capitalize!
# Objective : Capitalize first letter of first and last name
def solve(s):
    name = []
    for i in range(len(s.split())) :
        name.append(s.split()[i].capitalize())
    return " ".join(name)
#testing 
solve('hello  world  lol')