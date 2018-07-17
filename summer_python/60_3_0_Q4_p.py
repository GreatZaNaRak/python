n,k = int(input()) ,int(input())
std = [e for e in input().split()]
out = [std[0]]
j,run = 1,1
while (True) :
    if std[j%n] == std[0] and run % k == 0: break
    if j % k == 0 :
        out.append(std[j%n])
    j += 1 
    run += 1
print(*out)
