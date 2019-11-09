
def chessBoard(h,w,rs,cs):
    board = ''
    for r in range(h*(rs+1)+1):
        for c in range(w*(cs+1)+1):
            if r%(rs+1)==0 or c%(cs+1)==0 or (w*(cs+1))==c or (h*(rs+1))==r: cell = '*'
            else: cell = '.'
            board = board + cell
        board = board + '\n'
    return board
            
t = int(input())
for tp in range(t):
    h, w, rs, cs= input().split()
    print(chessBoard(int(h), int(w), int(rs), int(cs)))
