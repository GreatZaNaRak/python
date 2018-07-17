data = []
while True :
    get = int(input())
    if get == -1 : break
    data.append(get)
check = len(data)/2
count = [0]*len(data)
for i in range(len(data)):
    for j in range(len(data)):
        if data[i] == data[j] :
            count[i] += 1
result = []
for i in range(len(count)):
    if count[i] > check and data[i] not in result :
        result.append(data[i])
if len(result) == 0 : print('Not found')
else :
    for i in result :
        print(i)
#========================================================#
count = 0
data = []
while True :
    num = int(input())
    if num < 0 : break
    count += 1
    data.append(num)
f = count/2

check = []
result = []
for i in data :
    if i not in check :
        result.append(i)
        check.append(i)
check_data = [0]*len(result)
for i in result :
    for j in data :
        if i == j :
            check_data[result.index(i)] += 1
