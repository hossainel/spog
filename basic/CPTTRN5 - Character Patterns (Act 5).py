
def chessBoard(h,w,b):
    board = ''
    x = 0
    y = b+b
    for r in range(h*b+1):
        for c in range(w*b+1):
            if r%b==0 or c%b==0 or w*b==c or h*b==r: cell = '*'
            elif (r%(b+b)==x and c%(b+b)==x) or (r%(b+b)==(b+b-x) and c%(b+b)==(b+b-x)):
                cell = '\\'
            elif (r%(b+b)==y and c%(b+b)==(b+b-y)) or (r%(b+b)==(b+b-y) and c%(b+b)==y):
                cell = '/'
            else: cell = '.'
            board = board + cell
        board = board + '\n'
        if x == (b+b-1):
            x = 0
        else:
            x = x + 1
        if y == 1:
            y = b+b
        else:
            y = y - 1
    return board
            
t = int(input())
for tp in range(t):
    h, w, b= input().split()
    print(chessBoard(int(h), int(w), int(b)+1))
