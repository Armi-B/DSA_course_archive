from collections import deque
import sys
input = sys.stdin.readline
alpha_num = int(input())
req_num = int(input())

req_sequences = []
answers = [-1] * req_num

initial, temp_req = input().split()
req_sequences.append(temp_req)

for _ in range(req_num - 1):
    mappings = {}
    mapping, temp_req = input().split()
    for i in range(len(mapping)):
        mappings[mapping[i]] = initial[i]
    req = ''.join(mappings.get(c, c) for c in temp_req)
    req_sequences.append(req)

seen = {initial}
queue = deque()
queue.append(initial)
heights = deque()
heights.append(0)

while queue:
    # تا زمانی که متغییر خالی نشده ادامه میدهیم.
    done = True
    h = heights.popleft()
    curr = queue.popleft()

    for i in range(len(req_sequences)):
        if req_sequences[i] == curr and answers[i] == -1:
            answers[i] = h

    for i in range(alpha_num):
        for j in range(i + 1, alpha_num + 1):
            sub = curr[i:j]
            next_node = curr[:i] + sub[::-1] + curr[j:]
            if next_node not in seen:
                queue.append(next_node)
                heights.append(h + 1)
                seen.add(next_node)

    if all(ans != -1 for ans in answers):
        break

for ans in answers:
    print(ans)