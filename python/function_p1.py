def function1():
    sum = 0
    for i in range(10):
        sum += i
    return sum

def function2(n):
    i = 2
    if n == 1 :
        return False
    while i <= n**0.5 :
        if n % i == 0 :
            return False
        i += 1
    return True

def function3(n):
    for i in range(1,n):
        if function2(i):
            print(i)

def function4(x,y):
    match = 0
    notmatch = ''
    for i in x :
        if i == y :
            match += 1
        else :
            notmatch += i
    return [match,notmatch]
call = input().strip()
if call == 'function1' : print(function1())
elif call == 'function2' :
    n = int(input())
    print(function2(n))
elif call == 'function3' :
    n = int(input())
    function3(n)
else :
    a = [e for e in input().split()]
    print(function4(a[0],a[1]))
