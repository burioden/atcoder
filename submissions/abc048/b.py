a,b,x = map(int, input().split())

ans = 0

if a == b:
  if a%x == 0:
    ans = 1
  else:
    ans = 0
  
else:
  if a%x != 0:
    a = a-(a%x)+x
  elif b%x != 0:
    b = b-(b%x) 
  elif b-a == x:
    ans = 1
  ans = ((b-a)//x)+1

print(ans)
