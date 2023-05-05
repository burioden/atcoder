a,b,c,d = map(int, input().split())

if b >= c*d:
  print(-1)
  exit()

x = 1
while (b*x)+a > c*x*d:
  x += 1

print(x)
