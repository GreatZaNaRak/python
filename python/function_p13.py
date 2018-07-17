def row_number(t,e):
    result = 0
    for i in range(len(t)):
        if e in t[i] :
            result = i
            break
    return result

def flatten(t):
    result = [i for a in t for i in a if i != 0]
    return result

def inversions(x):
    a = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            a.append((x[i],x[j]))
    result = [i for i in a if i[0]>i[1]]
    return len(result)

def solvable(t):
    check = flatten(t)
    check = inversions(check)
    if len(t) % 2 != 0 :
        if check % 2 == 0 : return True
    elif len(t) % 2 == 0 :
        if check % 2 != 0 :
            if row_number(t,0) % 2 == 0 : return True
        elif check % 2 == 0 :
            if row_number(t,0) % 2 != 0 : return True
    return False

exec(input().strip())
