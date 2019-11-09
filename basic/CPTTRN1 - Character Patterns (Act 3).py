
def chessBoard(h,w):
    board = ''
    for r in range(h*3+1):
        for c in range(w*3+1):
            if r%3==0 or c%3==0 or (w*3)==c or (h*3)==r: cell = '*'
            else: cell = '.'
            board = board + cell
        board = board + '\n'
    return board
            
t = int(input())
for tp in range(t):
    h, w = input().split()
    print(chessBoard(int(h), int(w)))
