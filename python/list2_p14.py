n,c = [int(e) for e in input().split()]
data = []
for i in range(n):
    num = input().strip().split()
    data.append(num)
data_trans = []
for i in range(c):
    data_trans.append([])
for i in range(len(data_trans)):
    for j in range(len(data)):
        data_trans[i].append(data[j][i])
found = False
for i in data :
    get_low = min(i)
    index = i.index(get_low)
    high_location = data_trans[index]
    if get_low == max(high_location) :
        found = True
        break
if found : print(get_low)
else : print(-1)
    print(i,result[i])
