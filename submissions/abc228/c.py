n,k = map(int,input().split())
p = []
for i in range(n):
  p.append(sum(list(map(int, input().split()))))

x = sorted(p,reverse=True)[k-1]

for i in p:
  if x <= i + 300:
    print('Yes')
  else:
    print('No')
