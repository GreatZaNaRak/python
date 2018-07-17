n = int(input())
student_data = {}
score = []
capacity = {}
result = {}
for i in range(n) :
    text = input().strip().split()
    capacity[text[0]] = int(text[1])
m = int(input())
for i in range(m):
    text = input().strip().split()
    student_data[text[0]] = {'score':float(text[1]),'rank':text[2:]}
    score.append(float(text[1]))
score = sorted(score)[::-1]
for i in score :
    for j in student_data :
        if i == student_data[j]['score'] :
            for a in student_data[j]['rank'] :
                if capacity[a] != 0 :
                    result[j] = a
                    capacity[a] -= 1
                    break
for i in sorted(result):
    print(i,result[i])
