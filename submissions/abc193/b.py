n = int(input())
ans = 10**9 + 1
for i in range(n):
  a,p,x = map(int, input().split())
  if x > a:
    ans = min(ans,p)
    
print(ans if ans < 10**9 + 1 else -1)
