n = int(input())
data = []
for i in range(n):
    num = int(input())
    data.append(num)
result = sorted(data)
for i in result[::-1] :
    print(i)
