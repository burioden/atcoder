a = list(input().split())
a[0],a[2] = int(a[0]),int(a[2])

if a[1] == "+":
  print(a[0]+a[2])
else:
  print(a[0]-a[2])
