course = open(input().strip())
teacher = open(input().strip())
database = open(input().strip())
course_data = []
teacher_data = []
course_check = []
teacher_check = []
data = []
for line in course :
    line = line.strip()
    dict1 = {}
    line = line.split(',')
    dict1.update({'code_1':line[0],'subject':line[1]})
    course_data.append(dict1)
    course_check.append(line[0])
course.close()
for line in teacher :
    line = line.strip()
    dict1 = {}
    line = line.split(',')
    dict1.update({'code_2':line[0],'name':line[1]})
    teacher_data.append(dict1)
    teacher_check.append(line[0])
teacher.close()
for line in database :
    line = line.strip()
    dict1 = {}
    line = line.split(',')
    dict1.update({'interact_code_1':line[0],'interact_code_2':line[1]})
    data.append(dict1)
database.close()

result_1 = []
result_2 = []
for i in data :
    target_subject = i['interact_code_1']
    target_teacher = i['interact_code_2']
    for a in course_data :
        if target_subject in course_check :
            if a['code_1'] == target_subject :
                result_1.append(a['subject'])
        else : result_1.append('X');break
    for b in teacher_data :
        if target_teacher in teacher_check :
            if b['code_2'] == target_teacher :
                result_2.append(b['name'])
        else : result_2.append('X');break
for i in range(len(result_1)):
    start = result_1[i]
    stop = result_2[i]
    if start == 'X' or stop == 'X' :
        print('record error')
    else :
        print(start+','+stop)
