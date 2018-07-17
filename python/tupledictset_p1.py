n = int(input())
num = '0123456789'
data = []
for i in range(n):
    dic = {}
    infor = input().strip().split(':')
    dic.update({'id':infor[0],'location':infor[-1]})
    data.append(dic)
target = input().strip()
for i in data :
    if i['id'] == target :
        location_target = i['location']
location_target = location_target.strip()
set_target = set()
for a in location_target :
    if a not in ''' '.,"''' and a not in num:
        set_target.add(a)
printed = False
for i in data :
    if i['id'] != target :
        set_locate = set()
        for j in i['location'] :
            if j not in ''' '.,"''' and j not in num:
                set_locate.add(j)
        for b in set_locate :
            if b in set_target :
                print(i['id'])
                printed = True
                break
if not printed : print('Not Found')
