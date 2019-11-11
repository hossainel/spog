#upper co ordinate finder
def upperCo(uc):
    if uc[0]<=uc[2]:
        ux = uc[0]
    else:
        ux = uc[2]
    if uc[1]<=uc[3]:
        uy = uc[1]
    else:
        uy = uc[3]
    return ux, uy
#lower co ordinate finder
def lowerCo(lc):
    if lc[0]>=lc[2]:
        dx = lc[0]
    else:
        dx = lc[2]
    if lc[1]>=lc[3]:
        dy = lc[1]
    else:
        dy = lc[3]
    return dx, dy
#point
def p(x,y):
    ux = x
    uy = y
    dx = x
    dy = y
    return [ux, uy, dx, dy]
#circle
def c(x,y,r):
    ux = x - r
    uy = y - r
    dx = x + r
    dy = y + r
    return [ux, uy, dx, dy]
#line
def l(xy):
    ux, uy = upperCo(xy)
    dx, dy = lowerCo(xy)
    return [ux, uy, dx, dy]

#prints output of the ragtangle
def output(op):
    print(op[0],op[1],op[2],op[3])

t = int(input())
for tp in range(t):
    n = int(input())
    xop = []
    for np in range(n):
        tmp = input().split()
        st = tmp[0]
        x = int(tmp[1])
        y = int(tmp[2])
        if st == 'c':
            r = int(tmp[3])
            xop.append(c(x,y,r))
        elif st == 'l':
            x1 = int(tmp[3])
            y1 = int(tmp[4])
            xop.append(l([x,y,x1,y1]))
        else:
            xop.append(p(x,y))
    op = xop[0]
    for i in xop[1:]:
        op[0], op[1] = upperCo(i[:2]+op[:2])
        op[2], op[3] = lowerCo(i[2:]+op[2:])
    output(op)
