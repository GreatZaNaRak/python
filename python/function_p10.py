def distance(p,q):
    return ((p[0]-q[0])**2+(p[1]-q[1])**2)**0.5

def perimeter(points):
        sum1 = 0
        for i in range(len(points)):
            sum1 += distance(points[i-1],points[i])
        return sum1
    
s = input().strip().split()
p = [(float(t[1:t.find(',')]),float(t[t.find(',')+1:-1]))for t in s]
print(perimeter(p))
