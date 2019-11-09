
def chessBoard(h,w):
    board = ''
    for r in range(h):
        for c in range(w):
            if r==0 or c==0 or (w-1)==c or (h-1)==r: cell = '*'
            else: cell = '.'
            board = board + cell
        board = board + '\n'
    return board
            
t = int(input())
for tp in range(t):
    h, w = input().split()
    print(chessBoard(int(h), int(w)))
