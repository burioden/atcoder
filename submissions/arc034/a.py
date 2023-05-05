n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in a:
  i[4] *= (110/900)
  
ans = 0

for i in a:
  ans = max(ans, sum(i))
  
print(ans)
