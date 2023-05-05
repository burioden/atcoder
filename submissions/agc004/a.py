a = sorted(list(map(int,input().split())))

if sum(a)%2 == 1:
  print((a[0]*a[1]*((a[2]//2)+1)) - (a[0]*a[1]*(a[2]//2)))
else:
  print(0)
