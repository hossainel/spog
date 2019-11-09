
def chessBoard(h,w):
    board = ''
    for r in range(h):
        for c in range(w):
            if (r+c)%2==0: cell = '*'
            else: cell = '.'
            board = board + cell
        board = board + '\n'
    return board
            
t = int(input())
for tp in range(t):
    h, w = input().split()
    print(chessBoard(int(h), int(w)))
