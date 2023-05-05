n = int(input())
p = list(map(int,input().split()))

ans = [0]*n
for i in range(n):
  ans[p[i]-1] = i+1
  
print(*ans)
