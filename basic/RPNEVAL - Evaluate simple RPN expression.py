while(1):
    ix = input()
    if ix == '' or ix == ' ':
        break
    else:
        inp = ix.split()
    num = 0
    operator = 0
    for i in inp:
        if i == '+' or i=='-' or i=='*' or i=='/':
            operator = operator + 1
        else:
            num = num + 1
    if operator==num-1:
        c = 1
        result = 0.0
        for i in range(operator):
            for j in range(len(inp)-2):
                symbol = inp[j+2]
                a = float(inp[j])
                b = float(inp[j+1])
                if symbol=='+':
                    result = a + b
                    inp = inp[:j]+[result]+inp[j+3:]
                    break
                elif symbol=='-':
                    result = a - b
                    inp = inp[:j]+[result]+inp[j+3:]
                    break
                elif symbol=='*':
                    result = a * b
                    inp = inp[:j]+[result]+inp[j+3:]
                    break
                elif symbol=='/' and b==0.0:
                    result = 'ERROR'
                elif symbol=='/':
                    result = a / b
                    inp = inp[:j]+[result]+inp[j+3:]
                    break
                c = c + 1
        if result=='ERROR':
            print(result)
        else:
            print('%.4f'%result)
    else:
        print('ERROR')



