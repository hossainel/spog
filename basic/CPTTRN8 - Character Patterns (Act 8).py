
def chessBoard(h,w,b):
    board = ''
    for r in range(h*(b+b)):
        for c in range(w*(b+b)):
            x = (r+c)%(b+b+b+b)
            y = abs(r-c)%(b+b+b+b)
            b3 = b+b+b
            if (r+c)%(b+b)==b-1:
                cell = '/'
            elif abs(r-c)%(b+b)==b:
                cell = '\\'
            elif (x>=b and x<b3) and (y<=b or y>b3):
                cell = '*'
            elif (x<b or x>=b3) and (y>b and y<=b3):
                cell = '*'
            else: cell = '.'
            board = board + cell
        board = board + '\n'
    return board
            
t = int(input())
for tp in range(t):
    h, w, b= input().split()
    print(chessBoard(int(h), int(w), int(b)))

