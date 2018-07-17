def isSevenUp(x):
    if x % 7 == 0 or '7' in str(x) : return True
    return False

def nextSevenUp(x):
    while True :
        x += 1
        if x % 7 == 0 or '7' in str(x): return x

def prevSevenUp(x):
    while True :
        x -= 1
        if x % 7 == 0 or '7' in str(x) : return x

f,x = input().strip().split()
x = int(x)
if f == 'isSevenUp': print(isSevenUp(x))
elif f == 'nextSevenUp': print(nextSevenUp(x))
elif f == 'prevSevenUp':print(prevSevenUp(x))
