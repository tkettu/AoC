f = open("input.txt", "r")

#totals = {}

twos = 0
threes = 0

for l in f:
    totals = {}
    for c in l:
        totals[c] = totals.get(c, 0) + 1

    twosLeft = True
    threesLeft = True
    
    for k, v in totals.items():
        if (v == 2) & twosLeft:
            twos += 1
            twosLeft = False
        if (v == 3) & threesLeft:
            threes += 1
            threesLeft = False

t = twos * threes
print(t)
