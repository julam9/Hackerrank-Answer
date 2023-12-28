##Capitalize!
# Objective : Capitalize first letter of first and last name
def solve(s):
    name = []
    for i in range(len(s.split())) :
        name.append(s.split()[i].capitalize())
    return " ".join(name)
#testing 
solve('hello  world  lol')