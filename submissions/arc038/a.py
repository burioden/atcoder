n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

ans = 0

for i in range(0, n, 2):
  ans += a[i]
  
print(ans)
