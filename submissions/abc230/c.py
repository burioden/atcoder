n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

ans = []
# x+y == a+b or x+y == a-b
for x in range(p,q+1):
  inner = []
  for y in range(r,s+1):
    if x+y == a+b or x-y == a-b:
      inner.append('#')
    else:
      inner.append('.')
  ans.append(inner)
  
for i in ans:
  print(*i,sep='')

'''

問題文中の式がわけわかめ！な時はやってみればよい、の記録
 r1 = max(1-a,1-b)
 l1 = min(n-a,n-b)
 r2 = max(1-a,b-n)
 l2 = min(n-a,b-1)

 al = []
 bl = []

 for i in range(r1,l1+1):
   al.append([a+i,b+i])
  
 for i in range(r2,l2+1):
   bl.append([a+i,b-i])
  
 print(a+r1,b+r1,a+l1,b+l1)
 print(a+r2,b-r2,a+l2,b-l2)

'''
