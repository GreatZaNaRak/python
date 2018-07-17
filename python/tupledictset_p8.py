data = {}
list1 = [e for e in input().split()]
list2 = [e for e in input().split()]
for i in range(len(list1)):
    data[list1[i]] = list2[i]
    data[list2[i]] = list1[i]
target = [e for e in input().split()]
for i in target :
    if i in data : print(data[i],end=' ')
    else : print(i,end =' ')
#-------------------------------------------#
list1 = [e for e in input().split()]
list2 = [e for e in input().split()]
target = [e for e in input().split()]
result = []
for i in target :
    if i in list2 : result.append(list1[list2.index(i)])
    elif i in list1 : result.append(list2[list1.index(i)])
    else : result.append(i)
for j in result :
    print(j,end=' ')

