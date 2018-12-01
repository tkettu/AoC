inputFile = "d1aIn.txt"

data = open(inputFile, "r")

#data = [7, 7, -2, -7, -4]

freqs = [0]
s = 0

r = True
i = 0

while r:
    for d in data:
        s += int(d)
        
        if s in freqs:
            r = False
            break
        freqs.append(s)
    i += 1
    print('{0} loops done with {1} lenght and s = {2}'.format(i, len(freqs), s))
    data = open(inputFile, "r")
print(s)
