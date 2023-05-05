n = int(input())
x = list(map(int,input().split()))
m = round(sum(x)/n)

ans = 0
for i in x:
  ans += (i-m) ** 2

print(ans)
