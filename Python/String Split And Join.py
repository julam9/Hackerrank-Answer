##String split and join
# Objective : Given a string, split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    #split first and then join
    return "-".join(line.split(" "))
      
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    