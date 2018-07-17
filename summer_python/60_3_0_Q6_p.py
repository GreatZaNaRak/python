from collections import defaultdict as dic
data,d1,d2 = eval(input()) , dic(int) , dic(int)
for i in data :
    for j in data[i] :
        if j == "reactions" :
            for k in data[i][j] :
                d1[i] += data[i][j][k]
                d2[k] += data[i][j][k]

d1 = sorted([[i,j] for i,j in d1.items()],key = lambda x : x[-1])[::-1]
d2 = sorted([[i,j] for i,j in d2.items()],key = lambda x : x[-1])[::-1]
for i in d1 :
    print('id',i[0],'=',i[1])
print("---")
for i in d2:
    print(i[0],'=',i[1])

