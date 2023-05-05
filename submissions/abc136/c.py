n = int(input())
a = list(map(int,input().split()))[::-1]

x = a[0]
for i in range(1,n-1):
  if a[i] >= a[i+1] and x >= a[i+1]:
    x = min(a[i+1],x)
  else:
    if x < a[i+1] - 1:
      print('No')
      exit()
    else:
      continue

print('Yes')
