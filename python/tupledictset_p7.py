n = int(input())
dict1 = {}
infor = []
for i in range(n):
    text = input().strip()
    text = text.split()
    infor.append(text)
    if text[-1][0:2] in dict1 :
        dict1[text[-1][0:2]] += 1
    else :
        dict1[text[-1][0:2]] = 1
max_case = 0
target = []
for i in dict1 :
    if dict1[i] > max_case :
        max_case = dict1[i]
for i in dict1 :
    if dict1[i] == max_case :
        target.append(i)
target = sorted(target)
print(target[0])
print(max_case)
for i in infor :
    if i[-1][0:2] == target[0] :
        print(i[-1])
