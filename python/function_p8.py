def isSet(c1,c2,c3):
    check = True
    for i in range(len(c1)):
        if c1[i] == c2[i] and c1[i] == c3[i] and c2[i] == c3[i] or\
           c1[i] != c2[i] and c1[i] != c3[i] and c2[i] != c3[i] :
            pass
        else :
            check = False
    if check : return True
    return False

cards = []
for i in range(12):
    cards.append(input().strip().split())

for i in range(12):
    for j in range(i+1,12):
        for k in range(j+1,12):
            if isSet(cards[i],cards[j],cards[k]):
                print(i,j,k)
