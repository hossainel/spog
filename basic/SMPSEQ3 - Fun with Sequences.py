
input()
s = input().split()
input()
q = input().split()

tmp = []
ext = ''
Flag = True
for i in s:
    for j in q:
        if i==j:
            Flag = False
    if Flag:
        tmp.append(i)
    else:
        Flag = True

for i in tmp:
    ext = ext+i+' '

print(ext)
