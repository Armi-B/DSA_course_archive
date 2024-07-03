from collections import deque
import sys
input = sys.stdin.readline
rowsNum, colsNum, k = input().split()
rowsNum = int(rowsNum)
colsNum = int(colsNum)
k = int(k)

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = 'w'
        self.d = 0
    def discovery(self):
        self.c = 'g'

nodes = []

for i in range(k):
    y , x = input().split()
    y = int(y)
    x = int(x)
    nodes.append(Node(x,y))

def find_neighbor(nodes,x,y):
    neighbors = []
    for n in nodes:
        dx = n.x-x
        dy = n.y-y
        if abs(dx) <= 2 or abs(dy) <= 2:
            neighbors.append([n,dx,dy])

    return neighbors

solvable = False
lastLayer = []

queue = deque()
n = nodes[0]
n.discovery()
queue.append(n)
while queue:
    n = queue.popleft()
    if n.y >= rowsNum -2 or n.x >= colsNum - 2:
        solvable = True
        lastLayer.append(n)
    neighbors = find_neighbor(nodes,n.x, n.y)
    for i in neighbors:
        if i[0].c == 'w':
            i[0].discovery()
            if (i[1] == 0 and abs(i[2]) == 1) or (i[2] == 0 and abs(i[1]) == 1):
                queue.appendleft(i[0])
                i[0].d = n.d
            else:
                queue.append(i[0])
                i[0].d = n.d + 1

if solvable:
    mn = 0
    if (lastLayer[0].x == colsNum and lastLayer[0].y >= rowsNum -1) or (lastLayer[0].x >= colsNum - 1 and lastLayer[0].y == rowsNum):
        mn = lastLayer[0].d
    else:
        mn = lastLayer[0].d + 1
    for i in lastLayer:
        cost = i.d + 1
        if (i.x == colsNum and i.y >= rowsNum -1) or (i.x >= colsNum - 1 and i.y == rowsNum):
            cost = i.d
        if cost < mn:
            mn = cost        
    print(mn)
else:
    print(-1)