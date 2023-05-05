n,a,b = map(int,input().split())

ans = 0
if n < 3:
  if a==b:
    ans = 1
  else:
    ans = 0
elif a > b:
  ans = 0
else:
  x = n-2
  ans = (x*b)-(x*a)+1
  
print(ans)
