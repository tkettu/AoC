from collections import defaultdict

data = open("input.txt").read().split("\n")
data.sort()

def parseTime(line):
    return line.split(' ')[1].split(':')[1].strip(']')


guards = defaultdict(list)
sleepTime = defaultdict(int)
guard = 0
sleep = 0

for l in data:
    if l:
        time = int(parseTime(l))
        if 'Guard' in l:
            guard = l.split(' ')[3].strip('#')
            
        elif 'falls asleep' in l:
            sleep = time
        elif 'wakes up' in l:
            wake = time
            guards[guard].append((sleep, wake))
            sleepTime[guard] += (wake - sleep)

(guard, time) = max(sleepTime.items(), key=lambda i: i[1])
(minute, count) =  max([
    (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
    for minute in range(60)], key=lambda i: i[1])

print(guard)
print(minute)
print(guard * minute)
            
(guard, minute, count) = max([
    (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
    for minute in range(60) for guard in guards], key=lambda i: i[2])

print(guard)
print(minute)
print(int(guard)*int(minute))
