##The Minion Game
# Objective : Given string s, make substring. Kevin score substring which start with consonant, Stuart with vocal
def minion_game(string):
    n = len(string)
    vocal_letter = ['A', 'I', 'U', 'E', 'O']
    kevin_word = []
    stuart_word = []
    kevin_score = 0
    stuart_score = 0
    position = 0
    for i in s:
        if i in vocal_letter :
            for j in range(position, n):
                if : 
                    substring_score = 
                    kevin_score += substring_score
                else :
        else :
    
    if kevin_score > stuart_score :
        return "Kevin", kevin_score
    elif kevin_score < stuart_score:
        return "Stuart", stuart_word
    else : return "Draw"  