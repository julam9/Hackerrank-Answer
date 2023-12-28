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