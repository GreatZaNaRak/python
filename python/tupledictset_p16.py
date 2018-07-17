n = int(input())
data = []
for i in range(n):
    num = set([int(e) for e in input().split()])
    data.append(num)
if len(data) == 0 :
    print(0)
    print(0)
else :
    run_data = data[0]
    run_data_2 = data[0]
    for i in range(1,len(data)):
        infor = data[i]
        run_data = run_data.union(infor)
    for i in range(1,len(data)):
        infor_2 = data[i]
        run_data_2 = run_data_2.intersection(infor_2)
    print(len(run_data))
    print(len(run_data_2))
