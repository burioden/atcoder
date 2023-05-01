n = int(input())

ans = 0

for i in range(1,n+1):
  ans += i
  if n <= ans:
    print(i)
    break
