def add(d1,d2) :
    out = {}
    for i in d2 :
        if i not in d1 : d1[i] = d2[i]
        else : d1[i] += d2[i]
    for i in d1 :
        if d1[i] != 0 : out[i] = d1[i]
    return out
#-------------------------------------------------------
def common(x1,x2) :
    out = []
    for i in x1 :
        for j in x2 :
            if i == j : out.append(i)
    return sorted(out)
#-------------------------------------------------------
def get_zero_position(x) :
    out = set()
    for i in range(len(x)) :
        for j in range(len(x[i])) :
            if x[i][j] == 0 : out.add((i,j))
    return out
#-------------------------------------------------------
def a(n) :
    if n == 0 : return 2
    if n == 1 : return 1
    if n == 2 : return 0
    if n % 3 != 0 :
        return 2*a(n-3) + 1
    else :
        return 3*a(n-1)*a(n-2)-n**2
#-------------------------------------------------------
exec(input().strip())