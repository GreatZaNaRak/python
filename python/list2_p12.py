code,size = [int(e) for e in input().split()]
data = []
for i in range(size):
    data.append([])
for i in range(size):
    text = input().strip().split()
    for j in text :
        data[i].append(int(j))
result = []
if code == 1 :
    for i in range(len(data)):
        for j in range(i,len(data[i])):
            result.append(data[i][j])
elif code == 0 :
    data = data[::-1]
    check = len(data)
    for i in range(len(data)):
        for j in range(check):
            result.append(data[i][j])
        check -= 1
print(sum(result))
