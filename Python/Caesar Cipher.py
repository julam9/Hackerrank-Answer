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