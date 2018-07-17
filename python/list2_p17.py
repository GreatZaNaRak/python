data = []
score = []
while True :
    infor = [float(e) for e in input().split()]
    if len(infor) == 2 : data.append(infor); score.append(infor[1])
    elif len(infor) == 1 : target_to_find = infor[0] ; break
data = sorted(data)
score = sorted(score)[::-1]
check = []
while True :
    for i in range(len(data)-1):
        if data[i][-1] < data[i+1][-1] :
            data[i],data[i+1] = data[i+1],data[i]
    for i in data :
        check.append(i[-1])
    if check == score : break
    check = []
found = False
for i in range(len(data)) :
    if data[i][0] == target_to_find :
        found = True
        break
if found : print(i+1)
else : print('Not Found')
