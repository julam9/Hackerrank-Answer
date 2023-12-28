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