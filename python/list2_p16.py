n,c = [int(e) for e in input().split()]
vec1 = []
vec2 = []
result = []
for i in range(n):
    num1 = [int(e) for e in input().split()]
    vec1.append(num1)
for i in range(n):
    num2 = [int(e) for e in input().split()]
    vec2.append(num2)
for i in range(n):
    check = []
    for j in range(len(vec1[i])):
        check.append(vec1[i][j]+vec2[i][j])
    result.append(check)
for i in result :
    for j in i :
        print(j,end= ' ')
    print('',end='\n')
