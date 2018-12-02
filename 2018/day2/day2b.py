f = open("input.txt", "r")

#totals = {}

lines = []

#with open("input2.txt") as f:
for l in f:
    lines.append(l)

lLines =len(lines)
i = 0
chars1 = []
chars2 = []
notFound = True

while (i < lLines) & notFound:
    l = lines[i]
    j = i + 1
    ca1 = []
    i += 1
    for c in l:
        ca1.append(c)

    while(j < lLines):
        l2 = lines[j]
        ca2 = []
        j += 1
        for c2 in l2:
            ca2.append(c2)


        difference = 0
        
        for k in range(len(ca1)):
            if (ca1[k] != ca2[k]):
                difference += 1
            if difference > 1:
                break

        if (difference == 1):
           
            notFound = False
            chars1 = ca1
            chars2 = ca2
            break

print(chars1, chars2)

print(list(set(chars1) - set(chars2)))
print(''.join(chars1))

#
