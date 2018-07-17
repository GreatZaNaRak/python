def eat(q1,q2):
    if abs(q1[0]-q2[0]) == abs(q1[1]-q2[1]): return True
    if q1[0] == q2[0] or q1[1] == q2[1] : return True
    return False

def all_eat(L):
    result = []
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if eat(L[i],L[j]):
                result.append((i,j))
    return result

print(eval(input().strip()))
