n = int(input())
adj = [[] for _ in range(n+1)]

for i in range(n-1):
    u, v = input().split()
    u = int(u)
    v = int(v)
    adj [u].append(v)
    adj [v].append (u)

def dfs(adj, mark, h, v, b, way) :
    #اگر گره مورد نظر را یافتیم ان را برمیگردانیم.
    if v == b:
        way.insert(0, v)
        return h[v]
    mark[v] = 1
    #حلقه ای روی همسایه های گره میزنیم.
    for u in adj[v] :
        #راه های ممکن از هر همسایه را تا پایان امتحان میکنیم.
        if mark[u] == 0 :
            h[u] = h[v] + 1 
            r = dfs(adj, mark, h, u, b, way)
            if r != -1:
                way.insert(0, v)
                return r
    #اگر گره را نیافتیم -۱ برمیگردانیم.
    return -1

solvable = True
cost = 0
leafs = input().split()
ans = []
start = 1
first = True

for l in leafs:
    mark = [0] * (n + 1)
    h = [0] * (n + 1)
    way = []
    cost += dfs(adj, mark, h, start, int(l), way)
    if not first:
        way.pop(0)
    if cost> 2*n-2:
        solvable = False
        break
    ans = ans + way
    start = int(l)
    first = False

if solvable:
    mark = [0] * (n + 1)
    h = [0] * (n + 1)
    way = []
    cost += dfs(adj, mark, h, int(leafs[-1]), 1, way)
    if cost> 2*n-2:
        solvable = False
    way.pop(0)
    way.pop(-1)
    ans = ans + way

if solvable :
    #اگر شرط برقرار بود عناصر لیست را چاپ میکنیم.
    for el in ans:
        print(el, end=' ')
else:
    #در غیر این صورت -۱ را چاپ میکنیم.
    print(-1)