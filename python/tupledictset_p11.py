n = int(input())
infor = []
for i in range(n):
    text = input().strip().split()
    infor.append(text)
target = input().strip()
result = {}
out = []
for i in infor :
    if target in i :
        i = set(i)
        for j in i :
            if j in result :
                result[j] += 1
            else :
                result[j] = 1
if len(result) == 0 : print('Not Found')
else :
    for i in result :
        if i == target : pass
        else : out.append([i,result[i]])
    max_case = 0
    final = []
    for i in out :
        if i[-1] > max_case : max_case = i[-1]
    for i in out :
        if i[-1] == max_case :
            final.append(i)
    final = sorted(final)
    if len(final) == 0 : print('No suggested event')
    else :
        for j in final[0]:
            print(j)
