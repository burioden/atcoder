h,w = map(int,input().split())
a = []
for i in range(h):
  s = list(input())
  a.append(s)

a = zip(*a)

ans = []
for i in a:
  ans.append(i.count('#'))
  
print(*ans)
