import sys
sys.setrecursionlimit(10**6)

n,x,y = map(int, input().split())
g = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

ans = []

def dfs(now,pre):
  ans.append(now)
  if now == y:
    print(*ans)
    exit()
  for to in g[now]:
    if to != pre:
        dfs(to,now)
  # print(ans)
  # このans.popはどうしてちゃんと動くの…？
  ans.pop()

dfs(x,-1)
