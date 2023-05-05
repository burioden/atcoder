n,m = map(int,input().split())
s = [input() for _ in range(n)]
t = list(set([input() for _ in range(m)]))

cnt = 0

for i in t:
  for j in s:
    if j.endswith(i):
      cnt += 1
      
print(cnt)
