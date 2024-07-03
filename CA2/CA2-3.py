n = int(input())
intervals = []
temp = []
for i in range(n):
    e = int(input())
    if e == 0:
        intervals.append(temp.copy())
        temp.clear()
    else:
        temp.append(e)
if not len(temp) == 0:
    intervals.append(temp)

isSolvable = True
preSets = set(intervals[0])
for i in range(1,len(intervals)):
    newSet = set(intervals[i])
    if preSets.isdisjoint(newSet):
        preSets.union(newSet)
    else:
        isSolvable = False
        break;

if isSolvable:
    maxTime = 0
    for interval in intervals:
        startColor = {}
        endColor = {}
        repeated = []
        pre = 0
        for i in range(len(interval)):
            if interval[i] == pre:
                repeated.append(i)
                continue
            if not (interval[i] in startColor.keys()):
                startColor.update({interval[i]:i})
            endColor.update({interval[i]:i})
            pre = interval[i]
        s = []
        maxStackSize = 0
        isOnce = False
        if isSolvable:
            for i in range(len(interval)):
                maxStackSize = max(maxStackSize, len(s))
                if i in repeated:
                    continue
                if not(startColor[interval[i]]== i  or endColor[interval[i]]== i):
                    if not s[-1] == interval[i]:
                        isSolvable = False
                        break
                if startColor[interval[i]]== i  and endColor[interval[i]]== i:
                    isOnce = True
                if not(startColor[interval[i]]== i ) and endColor[interval[i]]== i:
                    if s[-1] == interval[i]:
                        s.pop()
                    else:
                        isSolvable = False
                        break
                if startColor[interval[i]]== i  and not(endColor[interval[i]]== i):
                    s.append(interval[i])
            if isOnce:
                maxStackSize += 1
        maxTime = max(maxStackSize , maxTime)
    if isSolvable:
        print(maxTime)
    else:
        print(-1)

