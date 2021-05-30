def getIdx(x,y):
    if(y > 200 and y < 450): # the first row
        if(x > 100 and x < 300): return 0
        if(x > 300 and x < 500): return 1
        if(x > 500 and x < 700): return 2

    if(y > 400 and y < 650): # the second row
        if(x > 100 and x < 300): return 3
        if(x > 300 and x < 500): return 4
        if(x > 500 and x < 700): return 5

    if(y > 600 and y < 850): # the third row
        if(x > 100 and x < 300): return 6
        if(x > 300 and x < 500): return 7
        if(x > 500 and x < 700): return 8


def getPosition():
    pass