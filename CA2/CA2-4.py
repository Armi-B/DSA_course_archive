
import sys
from collections import deque

def input_to_list( str):
    res = []
    num = ''
    for i in range(len(str)):
        if str[i] == ' ':
            res.append(int(num))
            num = ''
        else:
            num += str[i]
    res.append(int(num))
    return res

n = int(input())
jaygasht = input_to_list(input())

pos = [0 for _ in range(n + 1)]
for i in range(n):
    pos[jaygasht[i]] = i+1
pos[0] = sys.maxsize 
find = [[] for _ in range(n + 1)] 
stack = deque() 
boz = deque()
ku = deque()
for i in range(n, -1, -1):
    while (stack and stack[-1]>pos[i]):
        find[i].append(stack.pop())
    stack.append(pos[i])
for i in range(n):
    if (not boz) or jaygasht[i] < jaygasht[boz[-1]- 1]:
         boz.append(i + 1)

total = 0
for i in range(n):
    print(total)
    if (ku and ku[-1]>pos[i + 1]):
        total -= 1
    while (ku and ku[-1]>pos[i + 1]):
        ku.pop()
    rightLow = -1 if not ku else ku[-1]
    ku.append(pos[i + 1])
    boz.pop()
    if boz and boz[-1] > rightLow:
        total += 1
    for x in range(len(find[i + 1])-1, -1, -1):
        boz.append(find[i + 1][x])
print(0)
