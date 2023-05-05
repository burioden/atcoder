n,l = map(int,input().split())
a = list(map(int,input().split()))

for i in a:
  if i==2 and l < 2:
    print('No')
    exit()
  else:
    l -= i+1

print('Yes')
