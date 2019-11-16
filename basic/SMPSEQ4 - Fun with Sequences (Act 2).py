
input()
s = input().split()
input()
q = input().split()

tmp = []
ext = ''
for i in s:
    for j in q:
        if i==j:
            tmp.append(i)

for i in tmp:
    ext = ext+i+' '

print(ext)
