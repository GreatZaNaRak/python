num = [int(e) for e in input().split() ]
even_data = []
odd_data = []
out = []
for i in num :
    if i % 2 == 0 : even_data.append(i)
    else : odd_data.append(i)
even_data = sorted(even_data)
odd_data = sorted(odd_data)[::-1]
for i in range(len(num)):
    if len(even_data) != 0 :
        out.append(even_data[0])
        even_data.pop(0)
    else :
        out.append(odd_data[0])
        odd_data.pop(0)
for i in out :
    print(i,end= ' ')
