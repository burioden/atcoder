x,y = map(int,input().split())

if x < y:
  if (y-x)%10 != 0:
    print(((y-x)//10)+1)
  else:
    print((y-x)//10)
else:
  print(0)
