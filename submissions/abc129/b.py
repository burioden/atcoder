n = int(input())
w = list(map(int,input().split()))

ans = 101*101
for i in range(1,n):
  x = sum(w[0:i])
  y = sum(w[i:n])
  ans = min(ans,abs(x-y))
  
print(ans)
