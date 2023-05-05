a,b,k = map(int,input().split())

if a+b < k:
  a = 0
  b = 0
elif k > a:
  b = b-(k-a)
  a = 0
else:
  a -= k

print(a,b)
