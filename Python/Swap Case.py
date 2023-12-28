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