a,b,c,d = map(int, input().split())
n = int(input())

a = a*4
b = b*2
m = min(a,b,c)

if m*2 <= d:
  print(n*m)
else:
  if n%2 == 1:
    print((n//2)*d+m)
  else:
    print((n//2)*d)
