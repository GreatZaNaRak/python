from string import ascii_lowercase as l
from string import ascii_uppercase as h
num = "0123456789"
n = int(input())
out = []
for i in range(n) :
    count = 0
    text = input().strip()
    for j in range(len(text)) :
        if text[j] == ',' :
            if not(text[j-1] in l+h+num and text[j+1] == " " \
            and text[j+2] in l+h+num) :
                count += 1
    out.append(count)
print(*out,sep='\n')