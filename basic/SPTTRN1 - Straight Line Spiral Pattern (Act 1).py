
import math
def snake(n):
    x = n
    straight = True
    board = ''
    for r in range(n):
        for c in range(n):
            if ((r+c)%n>=r and r<=c+1) and r%2==0 and r<math.ceil(n/2):#up
                cell = '*'
            elif  ((r+c+1)%n<=r and r<=c) and (n+c)%2: #right*
                cell = '*'
            elif ((r+c+1)%n<=r and r>=c) and (n+r)%2 and (r>n//2): #down*
                cell = '*'
            elif ((r+c)%n>=r and r>c+1) and c%2==0 and (c<n//2): #left*
                cell = '*'
            else:
                cell = '.'
            board = board + cell
        board = board +'\n'

    return board

t = int(input())
for tp in range(t):
    s = int(input())
    board = snake(s)
    print(board)
    
    
