n, m = input().split()
n = int(n)
m = int(m)

adj = [[] for _ in range(n+1)]
colorList = [[] for _ in range(n+1)]

for i in range(m):
    u, v = input().split()
    u = int(u)
    v = int(v)
    adj [u].append(v)
    adj [v].append (u)

for i in range(1, n+1):
    coloredEnemy = 0
    for j in adj[i]:
        if not (not colorList[j]):
            coloredEnemy = j
    if coloredEnemy == 0:
        colorList[i].append(0)
    else:
        colorList[i].append(1 -  colorList[coloredEnemy][0])

g1 = []
g1Size = 0

for i in range(len(colorList)):
    if colorList[i] == [0]:
        g1Size += 1
        g1.append(i)

print(g1Size)
for el in g1:
    print(el, end=' ')
