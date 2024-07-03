import sys
from collections import deque

N = int(input())
p = [int(x) for x in input().split()]
Pos = [0] * (N + 1)

for i in range(N):
    Pos[p[i]] = i + 1
Pos[0] = sys.maxsize 

find = [[] for _ in range(N + 1)] 
Stack = deque() 
for i in range(N, -1, -1):
    while Stack and Stack[-1] > Pos[i]:
        find[i].append(Stack.pop())
    Stack.append(Pos[i])

Boz = deque()
Koo = deque()
for i in range(N):
    if not Boz or p[i] < p[Boz[-1] - 1]:
        Boz.append(i + 1)
total = 0
for i in range(N):
    print(total)
    if Koo and Koo[-1] > Pos[i + 1]:
        total -= 1
    while Koo and Koo[-1] > Pos[i + 1]:
        Koo.pop()
    rightLow = -1 if not Koo else Koo[-1]
    Koo.append(Pos[i + 1])
    Boz.pop()
    if Boz and Boz[-1] > rightLow:
        total += 1
    for j in range(len(find[i + 1]) - 1, -1, -1):
        Boz.append(find[i + 1][j])
print("0")