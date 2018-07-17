n = int(input())
data = []
for i in range(n) :
    dic = {}
    infor = input().strip().split(', ')
    dic.update({'id':infor[0],'subject':infor[1:]})
    data.append(dic)
target = input().strip().split(', ')
result = []
check = []
out = ''
for i in target :
    dic = {}
    for j in data :
        if i in j['subject'] :
            check.append(j['id'])
    for b in check :
        out += b+', '
    dic.update({'subject_run':i,'student_registed':out[:-2]})
    result.append(dic)
    check = []
    out = ''
for i in result :
    if len(i['student_registed']) != 0 :
        print(i['subject_run']+' -> '+i['student_registed'])
    elif len(i['student_registed']) == 0 :
        print(i['subject_run']+' -> '+'Not found')
