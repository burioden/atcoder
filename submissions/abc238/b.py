n = int(input())
a = list(map(int,input().split()))

c = [0,360]

for i in a:
  c.append((c[-1]+i)%360)

c.sort()

ans = 0
for i in range(1,len(c)):
  x = c[i] - c[i-1]
  ans = max(x,ans)

print(ans)
