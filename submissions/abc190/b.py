n,s,d = map(int,input().split())

for i in range(n):
  x,y = map(int, input().split())
  if x < s and y > d:
    print('Yes')
    exit()
    
print('No')
