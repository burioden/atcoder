n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

x = max(a)

flg = 0
for i in range(k):
  if a[b[i]-1] == x:
    flg = 1
    break
    
print('Yes' if flg else 'No')
