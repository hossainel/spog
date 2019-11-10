
def chessBoard(h,w,b,l):
    board = ''
    for r in range((h+1)*(b+1)-1):
        for c in range((w+1)*(l+1)-1):
            if (r+1)%(b+1)==0 and (c+1)%(l+1)==0:
                cell = '+'
            elif (r+1)%(b+1)==0 and r>0:
                cell = '-'
            elif (c+1)%(l+1)==0 and c>0:
                cell = '|'
            else: cell = '.'
            board = board + cell
        board = board + '\n'
    return board
            
t = int(input())
for tp in range(t):
    h, w, b, l= input().split()
    print(chessBoard(int(h), int(w), int(b), int(l)))
