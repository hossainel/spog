t = int(input())

def half(k):
    l = len(k)
    s = k[0]
    h = l//2
    hs = k[:h]
    g = 2
    while(g<len(hs)):
        s = s + hs[g]
        g = g + 2
        h = h//2
    return s

for i in range(t):
    k = input()
    print(half(k))
    
