n = int(input())
data = {}
result = []
for i in range(n):
    num = input().strip()
    if num in data.keys() : data[num] += 1
    else : data[num] = 1
max_case = 0
for i in data :
    if data[i] > max_case : max_case = data[i]
for i in data :
    if data[i] == max_case : result.append(i)
print(sorted(result)[0])
