file = open('score.txt','r')
data = []
for line in file :
    line = line.strip()
    line = line.split()
    data.append(line)
file.close()
out = ''
while True :
    text = input().strip()
    if text == '-1' :
        break
    for c in data :
        found = False
        if c[0] == text :
            out += c[-1]+'/'
            found = True
            break
    if not found : out += 'Not Found/'
out = out[:-1]
for i in out :
    if i == '/' : print('')
    else : print(i,end = '')
