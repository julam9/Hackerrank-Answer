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
        