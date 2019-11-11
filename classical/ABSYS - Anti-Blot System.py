#number + number = number
def divider(n):
    #a + b = c
    a = n.split('+')[0]
    b, c = n.split('+')[1].split('=')
    if 'machula' in a:
        print(str(int(c)-int(b))+' +'+b+'='+c)
    elif 'machula' in b:
        print(a+'+ '+str(int(c)-int(a))+' ='+c)
    else:
        print(a+'+'+b+'= '+str(int(a)+int(b)))
        
inp = int(input())
input()
for i in range(inp):
    d = input()
    divider(d)
    if i==inp-1:
        pass
    else:
        input()
