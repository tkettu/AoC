inputFile = "d1aIn.txt"

data = open(inputFile, "r")

s = 0

for d in data:
    s += int(d)

print(s)
