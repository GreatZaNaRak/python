num = [e for e in input().split()]
check = set(num)
result = []
count = 0
for i in check :
    for j in num :
        if i == j : count += 1
        if count > 1 : break
    if count == 1 : result.append(int(i))
    count = 0
if len(result) == 0 : print('NONE')
else : print(min(result))
