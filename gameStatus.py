def getGameState(inputs):
    #check if the game is tie
    isFull = True
    for input in inputs:
        if(input == ''): 
            isFull = False
    if(isFull):
        return 'Tie'
    else:
        #the game rules
        if(inputs[0] == inputs[1] == inputs[2] and inputs[0] != ''): return inputs[0]
        elif(inputs[3] == inputs[4] == inputs[5] and inputs[3] != ''): return inputs[3]
        elif(inputs[6] == inputs[7] == inputs[8] and inputs[6] != ''): return inputs[6]
        elif(inputs[0] == inputs[3] == inputs[6] and inputs[0] != ''): return inputs[0]
        elif(inputs[1] == inputs[4] == inputs[7] and inputs[1] != ''): return inputs[1]
        elif(inputs[2] == inputs[5] == inputs[8] and inputs[2] != ''): return inputs[2]
        elif(inputs[0] == inputs[4] == inputs[8] and inputs[0] != ''): return inputs[0]
        elif(inputs[2] == inputs[4] == inputs[6] and inputs[2] != ''): return inputs[2]
            