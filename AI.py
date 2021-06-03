from gameStatus import getGameState

global scores 
scores = {'X': -1, 'O': 1, 'Tie' : 0}

def minimax(inputs, depth, isMaximizing):
    result = getGameState(inputs)
    if(result != None):
        return scores[result]
    
    if(isMaximizing):
        bestScore = -999999
        for i in range(0,9):
            if(inputs[i] == ''):
                inputs[i] = 'O'
                score = minimax(inputs, depth + 1, False)
                inputs[i] = ''
                bestScore = max(score,bestScore)
        return bestScore
    else:
        bestScore = 999999
        for i in range(0,9):
            if(inputs[i] == ''):
                inputs[i] = 'X'
                score = minimax(inputs, depth + 1, True)
                inputs[i] = ''
                bestScore = min(score,bestScore)
        return bestScore


def computerChoice(inputs):
    maxScore = -999999
    global bestMove
    for i in range(0,9):
        if(inputs[i] == ''):
            inputs[i] = 'O'
            score = minimax(inputs, 0, False)
            inputs[i] = ''
            if score > maxScore:
                maxScore = score
                bestMove = i
    return bestMove

