n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

l = max(a)
r = min(b)

if r-l+1 <= 0:
  print(0)
else:
  print(r-l+1)
