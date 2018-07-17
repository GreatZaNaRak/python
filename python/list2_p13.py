n = int(input())
c = int(input())
data = []
for i in range(n):
    num = input().strip().split()
    data.append(num)
found = False
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i] == data[j] :
            found = True
            index_to_find = i
            index_found = j
            break
    if found : break
if found :
    print(index_to_find+1)
    for i in data[index_to_find] :
        print(i,end=' ')
    print('',end='\n')
    print(index_found+1)
    for i in data[index_found]:
        print(i,end=' ')
