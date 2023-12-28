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