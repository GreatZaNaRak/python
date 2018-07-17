n = int(input())
data = []
for i in range(n):
    num = float(input())
    data.append(num)
data = sorted(data)
check_mode = [0]*len(data)
arvg = sum(data)/n
if len(data) % 2 != 0 :
    med = data[(len(data))//2]
else :
    med = (data[len(data)//2]+data[len(data)//2-1])/2
for i in range(len(data)):
    num_check = data[i]
    for j in range(i+1,len(data)):
        if data[j] == num_check :
            check_mode[i] += 1
max_index = 0
for i in range(len(check_mode)) :
    word = check_mode[i]
    if word > check_mode[max_index] :
        max_index = i
mode = int(data[max_index])
print(arvg,med,mode)
