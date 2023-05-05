n = int(input())
a = [[*input()] for _ in range(n)]
ans = 0

for i in range(n):
  for j in range(n):
    for x,y in [(1,0),(0,1),(1,1),(1,-1)]:
      s = ""
      for k in range(n):
        s += a[(i+k*x)%n][(j+k*y)%n]
      ans = max(ans,int(s),int(s[::-1]))

print(ans)
