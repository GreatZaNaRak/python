num = set([int(e) for e in input().split()])
result = int(input())
count = 0
for i in num :
    target = result-i
    if target in num : count += 1
print(count//2)
