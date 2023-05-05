n,m,t = map(int,input().split())
c = n
u = 0

# c は 「bからc進んだらバッテリー滅するよ」
# u は 出発地点
for i in range(m):
  a,b = map(int,input().split())
  if c <= a-u:
    print('No')
    exit()
  c = min(c+b - 2*a + u,n)
  u = b

print('Yes' if t-u < c else 'No')
