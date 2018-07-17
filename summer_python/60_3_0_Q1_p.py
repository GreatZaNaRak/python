import math as m
x,y = [float(e) for e in input().split()]
print(((4*x**3+3*y**2)/((m.e)**x+(m.e)**y)) + ((m.log(abs(x+10**-3),m.pi))/(m.sqrt(8))))