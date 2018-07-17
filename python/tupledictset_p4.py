num = [int(e) for e in input().split()]
result = int(input())
count = 0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == result : count += 1
print(count)
