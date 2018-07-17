data = {}
check = []
n = int(input())
for i in range(n):
    get = input().split()
    data[get[0]] = set(get[1:])
    check.append(get)
target = set([e for e in input().split()])
result = []
for i in data :
    if target.issubset(data[i]):
        result.append(i)
printed = False
for i in sorted(result):
    for j in check :
        if i == j[0] :
            print(' '.join(j))
            printed = True
if not printed : print('Not Found')
#-------------------------------------------------#
n = int(input())
data = []
result = []
out = ''
final = []
for i in range(n):
    dict1 = {}
    out = ''
    text = input().strip().split()
    out += ' '+text[1]+' '+text[2]+' '+text[3]+' '
    dict1.update({'name':text[0],'infor':out})
    data.append(dict1)
target = [e for e in input().split()]
for i in data :
    found = True
    for j in target :
        if ' '+j+' ' not in i['infor'] : found = False;break
    if found : result.append(i)
for i in result :
    final.append(i['name']+i['infor'])
final = sorted(final)
printed = False
for i in final :
    print(i)
    printed = True
if not printed : print('Not Found')
