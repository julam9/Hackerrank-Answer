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