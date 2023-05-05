n,q = map(int,input().split())
s = list(input())

i = 0
for j in range(q):
  a,b = map(int,input().split())
  if a == 1:
    i -= b
  else:
    print(s[(i+b-1)%n])
