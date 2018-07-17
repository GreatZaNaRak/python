c = [0]*62
text = input().strip()
for i in text :
    if '0' <= i <= '9' : c[int(i)] += 1
    else :
        if i == 'A' : c[10] += 1
        elif i == 'B' : c[11] += 1
        elif i == 'C' : c[12] += 1
        elif i == 'D' : c[13] += 1
        elif i == 'E' : c[14] += 1
        elif i == 'F' : c[15] += 1
        elif i == 'G' : c[16] += 1
        elif i == 'H' : c[17] += 1
        elif i == 'I' : c[18] += 1
        elif i == 'J' : c[19] += 1
        elif i == 'K' : c[20] += 1
        elif i == 'L' : c[21] += 1
        elif i == 'M' : c[22] += 1
        elif i == 'N' : c[23] += 1
        elif i == 'O' : c[24] += 1
        elif i == 'P' : c[25] += 1
        elif i == 'Q' : c[26] += 1
        elif i == 'R' : c[27] += 1
        elif i == 'S' : c[28] += 1
        elif i == 'T' : c[29] += 1
        elif i == 'U' : c[30] += 1
        elif i == 'V' : c[31] += 1
        elif i == 'W' : c[32] += 1
        elif i == 'X' : c[33] += 1
        elif i == 'Y' : c[34] += 1
        elif i == 'Z' : c[35] += 1
        elif i == 'a' : c[36] += 1
        elif i == 'b' : c[37] += 1
        elif i == 'c' : c[38] += 1
        elif i == 'd' : c[39] += 1
        elif i == 'e' : c[40] += 1
        elif i == 'f' : c[41] += 1
        elif i == 'g' : c[42] += 1
        elif i == 'h' : c[43] += 1
        elif i == 'i' : c[44] += 1
        elif i == 'j' : c[45] += 1
        elif i == 'k' : c[46] += 1
        elif i == 'l' : c[47] += 1
        elif i == 'm' : c[48] += 1
        elif i == 'n' : c[49] += 1
        elif i == 'o' : c[50] += 1
        elif i == 'p' : c[51] += 1
        elif i == 'q' : c[52] += 1
        elif i == 'r' : c[53] += 1
        elif i == 's' : c[54] += 1
        elif i == 't' : c[55] += 1
        elif i == 'u' : c[56] += 1
        elif i == 'v' : c[57] += 1
        elif i == 'w' : c[58] += 1
        elif i == 'x' : c[59] += 1
        elif i == 'y' : c[60] += 1
        elif i == 'z' : c[61] += 1
for i in c :
    print(i,end= ' ')
