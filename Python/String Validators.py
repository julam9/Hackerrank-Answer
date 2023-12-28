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