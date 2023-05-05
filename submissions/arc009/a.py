n = int(input())
ans = 0
for i in range(n):
  a,b = map(int,input().split())
  ans += (a*b)
  
tax = ans * 0.05

print(int(ans + tax))
