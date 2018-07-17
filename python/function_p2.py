def nextEven(f):
    import math as m
    even = m.ceil(f)
    if even % 2 == 0 : even += 1.0
    else : pass
    return int(even)
def nextOdd(f):
    import math as m
    odd = m.ceil(f)
    if odd % 2 == 0 : pass
    else : odd += 1.0
    return int(odd)
while True :
    x = float(input())
    if x < 0 : break
    even = nextEven(x)
    odd = nextOdd(x)
    print((odd,even))
