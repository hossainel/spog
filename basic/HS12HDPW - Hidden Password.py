
def hiddenPassword(key, bascii):
    password = ''
    for i in bkey:
        kn = 5
        a = ''
        b = ''
        for j in i.encode('ascii'):
            kx = str(bin(j))[2:]
            kx = '0'*(8-len(kx))+kx
            kx = kx[2:]
            a = kx[kn] + a              
            b = kx[(kn+3) % 6] + b
            kn = kn - 1
        password = password + bascii[int(a, 2)]+bascii[int(b, 2)]
    return password

t = int(input())
for tp in range(t):
    blen = input()
    if blen=='' or ' ': blen = input()
    bkey = input().split()
    bascii = input()
    password = hiddenPassword(bkey, bascii)
    print(password)

