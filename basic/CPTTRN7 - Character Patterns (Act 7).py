
def chessBoard(h,w,b):
    board = ''
    x=0
    y=b+b
    for r in range(h*(b+b)):
        for c in range(w*(b+b)):
            if r%(b+b)==x and (c%(b+b)==b+x or c%(b+b)==b-y):
                cell = '\\'
            elif r%(b+b)==x and (c%(b+b)==b-x-1 or c%(b+b)==b+y-1):
                cell = '/'
            else: cell = '.'
            board = board + cell
        board = board + '\n'
        if x==b+b-1:
            x = 0
        else:
            x = x + 1
        if y==1:
            y=b+b
        else:
            y = y - 1
    return board
            
t = int(input())
for tp in range(t):
    h, w, b= input().split()
    print(chessBoard(int(h), int(w), int(b)))

