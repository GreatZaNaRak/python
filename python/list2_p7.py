file = open('score.txt','r')
data = []
check = []
for line in file :
    line = line.strip()
    line = line.split()
    data.append(int(line[0]))
data = sorted(data)
for i in data :
    print(i)
