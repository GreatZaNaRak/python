n,c = [int(e) for e in input().split()]
data = []
for i in range(n):
    data.append([])
for i in range(len(data)) :
    text = input().split()
    for j in text :
        data[i].append(j)
for i in range(len(data)):
    summation = 0
    count = 0
    for j in data[i] :
        if j == 'A' : summation += 4 ; count += 1
        elif j == 'B+' : summation += 3.5 ; count += 1
        elif j == 'B' : summation += 3 ; count += 1
        elif j == 'C+' : summation += 2.5 ; count += 1
        elif j == 'C' : summation += 2 ; count += 1
        elif j == 'D+' : summation += 1.5 ; count += 1
        elif j == 'D' : summation += 1 ; count += 1
        elif j == 'F' : summation += 0 ; count += 1
        elif j == 'X' : summation += 0
    print("{:.2f}".format(summation/count))
