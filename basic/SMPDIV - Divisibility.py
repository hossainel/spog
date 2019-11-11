
t = int(input())
for tp in range(t):
    tmp = input().split()
    n = int(tmp[0])
    x = int(tmp[1])
    y = int(tmp[2])
    numlist = ''
    if x>n or x%y==0:
        pass
    else:
        for i in range(x, n+1):
            if i%x==0 and i%y!=0:
                numlist = numlist + str(i) + ' '

    print(numlist)
