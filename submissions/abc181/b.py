n = int(input())
ans = 0
for i in range(n):
  a,b = map(int,input().split())
  x = (a+b)*(b-a+1)//2
  ans += x

print(ans)
