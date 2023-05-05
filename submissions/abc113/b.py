n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))

ans = [0]*n
for i,d in enumerate(h):
  x = a-(t-d * 0.006)
  if x < 0:
    x *= -1
  ans[i] = x

print(ans.index(min(ans))+1)
