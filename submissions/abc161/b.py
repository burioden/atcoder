n,m = map(int,input().split())
a = list(map(int,input().split()))

s = sum(a)

cnt = n
for i in a:
  if i < s / (4*m):
    cnt -= 1
  
print('Yes' if cnt >= m else 'No')
