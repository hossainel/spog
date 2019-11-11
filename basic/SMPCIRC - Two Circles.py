
import math

t = int(input())
for tp in range(t):
    tmp = input().split()
    x1 = int(tmp[0])
    y1 = int(tmp[1])
    r1 = int(tmp[2])
    x2 = int(tmp[3])
    y2 = int(tmp[4])
    r2 = int(tmp[5])
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if distance == float(r1+r2) or distance == float(abs(r1-r2)):
        print('E')
    elif distance <= float(abs(r1-r2)):
        print('I')
    else:
        print('O')
