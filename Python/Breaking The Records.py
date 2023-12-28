##Breaking the Records
# Objective : Given Maria record of point scored, determine how many times Maria breaks her record for most and least points during the season
def breakingRecords(scores):
    n = len(scores)
    #how many times max scored breaked
    max_record = [scores[i+1] for i in range(n-1) if max(scores[:i+1]) < scores[i+1]]
    #hwo many times min scored breaked
    min_record = [scores[i+1] for i in range(n-1) if min(scores[:i+1]) > scores[i+1]]
    return(len(max_record), len(min_record))    
#testing 
breakingRecords([1,10,5,1,6,99,100,101,5])