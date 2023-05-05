n = int(input())
ans = []
for i in range(n):
  x,y = input().split()
  x = float(x)
  if y=="BTC":
    x *= 380000.0
  ans.append(x)

print(sum(ans))
