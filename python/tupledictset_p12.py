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
    store = []
    for i in out :
        store.append(i[-1])
    store = sorted(store)[::-1]
    out = sorted(out)
    while True :
        check = []
        for i in out :
            check.append(i[-1])
        if check == store : break
        for i in range(len(out)-1):
            if out[i][-1] < out[i+1][-1] :
                out[i],out[i+1] = out[i+1],out[i]
    if len(out) == 0 : print('No suggested event')
    else :
        for i in out :
            print(str(i[0])+' '+str(i[-1]))
