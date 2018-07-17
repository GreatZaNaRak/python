n = int(input())
data = []
for i in range(n):
    num = input().strip().split()
    data.append(num)
found = False
out = ''
for i in range(len(data)):
    for j in range(len(data)):
        out += data[j][i]
    if out == '1'*n :
        found = True
        break
    out = ''
if found : print(i)
else : print(-1)
