def getIdx(x,y):
    if(y > 200 and y < 400): # the first row
        if(x > 100 and x < 300): return 0
        if(x > 300 and x < 500): return 1
        if(x > 500 and x < 700): return 2

    if(y > 400 and y < 600): # the second row
        if(x > 100 and x < 300): return 3
        if(x > 300 and x < 500): return 4
        if(x > 500 and x < 700): return 5

    if(y > 600 and y < 800): # the third row
        if(x > 100 and x < 300): return 6
        if(x > 300 and x < 500): return 7
        if(x > 500 and x < 700): return 8


def getCenter(idx):
    #first row
    if(idx == 0): return [195,300]
    if(idx == 1): return [395,300]
    if(idx == 2): return [595,300]
    #second row
    if(idx == 3): return [195,500]
    if(idx == 4): return [395,500]
    if(idx == 5): return [595,500]
    #third row
    if(idx == 6): return [195,695]
    if(idx == 7): return [395,695]
    if(idx == 8): return [595,695]